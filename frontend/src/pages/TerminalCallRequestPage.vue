<template>
  <div class="container">
    <call-header></call-header>
    <div class="video-container">
      <video ref="localVideo" autoplay muted class="video"></video>
      <video ref="remoteVideo" autoplay class="video remote-video"></video>
      <div class="button-container">
        <default-button @click="startWebCamera" title="Включить веб-камеру">
          <font-awesome-icon icon="fa-solid fa-video fa-fw" />
        </default-button>
        <default-button @click="startScreenShare" title="Включить демонстрацию экрана">
          <font-awesome-icon icon="fa-solid fa-display" />
        </default-button>
        <default-button @click="call" :disabled="!isCallEnabled" title="Начать звонок">
          <font-awesome-icon icon="fa-solid fa-phone" />
        </default-button>
        <default-button @click="hangup, $router.push('/terminal')" title="Завершить звонок">
          <font-awesome-icon icon="fa-solid fa-phone-slash" />
        </default-button>
        <default-button @click="toggleMicrophone">
          <span v-if="!isMicrophoneActive">
            <font-awesome-icon icon="fa-solid fa-microphone fixed-width" />
          </span>
          <span v-if="isMicrophoneActive">
            <font-awesome-icon icon="fa-solid fa-microphone-slash" fixed-width />
          </span>
        </default-button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      localStream: null,
      remoteStream: new MediaStream(),
      peerConnection: null,
      signalingServerUrl: 'ws://localhost:8000/ws/myroom',
      iceServers: {
        iceServers: [{ urls: 'stun:stun.l.google.com:19302' }],
      },
      socket: null,
      isMicrophoneActive: true, // Состояние микрофона
    }
  },
  computed: {
    isCameraActive() {
      return this.localStream && this.localStream.getVideoTracks().length > 0
    },
    isScreenSharingActive() {
      return this.localStream && this.localStream.getVideoTracks().length === 0
    },
    isCallEnabled() {
      return this.localStream !== null
    },
    isCallActive() {
      return this.peerConnection !== null
    },
  },
  mounted() {
    this.setupWebSocket()
  },
  methods: {
    setupWebSocket() {
      this.socket = new WebSocket(this.signalingServerUrl)

      this.socket.onmessage = async (message) => {
        const data = JSON.parse(message.data)
        if (data.offer) {
          await this.handleOffer(data.offer)
        } else if (data.answer) {
          await this.handleAnswer(data.answer)
        } else if (data.candidate) {
          await this.handleCandidate(data.candidate)
        }
      }
    },

    async startWebCamera() {
      this.localStream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true })
      this.$refs.localVideo.srcObject = this.localStream
    },

    async startScreenShare() {
      this.localStream = await navigator.mediaDevices.getDisplayMedia()
      this.$refs.localVideo.srcObject = this.localStream
    },

    async call() {
      this.peerConnection = new RTCPeerConnection(this.iceServers)
      this.$refs.remoteVideo.srcObject = this.remoteStream

      // Добавление локального потока в PeerConnection
      this.localStream
        .getTracks()
        .forEach((track) => this.peerConnection.addTrack(track, this.localStream))

      this.peerConnection.onicecandidate = (event) => {
        if (event.candidate) {
          this.socket.send(JSON.stringify({ candidate: event.candidate }))
        }
      }

      this.peerConnection.ontrack = (event) => {
        this.remoteStream.addTrack(event.track)
      }

      // Создание оффера
      const offer = await this.peerConnection.createOffer()
      await this.peerConnection.setLocalDescription(offer)
      this.socket.send(JSON.stringify({ offer }))
    },

    hangup() {
      if (this.peerConnection) {
        this.peerConnection.close()
        this.peerConnection = null
        // Можно добавить логику для закрытия сокета, если это необходимо
        // this.socket.close();
        // Очистка локального потока
        if (this.localStream) {
          const tracks = this.localStream.getTracks()
          tracks.forEach((track) => track.stop())
          this.localStream = null
        }
        // Сброс состояния
        this.$refs.localVideo.srcObject = null
        this.$refs.remoteVideo.srcObject = null
      }
    },

    async handleOffer(offer) {
      this.peerConnection = new RTCPeerConnection(this.iceServers)

      // Обработка ICE-кандидатов
      this.peerConnection.onicecandidate = (event) => {
        if (event.candidate) {
          this.socket.send(JSON.stringify({ candidate: event.candidate }))
        }
      }

      // Обработка входящего видеопотока
      this.peerConnection.ontrack = (event) => {
        this.remoteStream.addTrack(event.track)
      }

      await this.peerConnection.setRemoteDescription(new RTCSessionDescription(offer))

      const answer = await this.peerConnection.createAnswer()
      await this.peerConnection.setLocalDescription(answer)

      // Отправка ответа обратно на сервер
      this.socket.send(JSON.stringify({ answer }))
    },

    async handleAnswer(answer) {
      await this.peerConnection.setRemoteDescription(new RTCSessionDescription(answer))
    },

    async handleCandidate(candidate) {
      await this.peerConnection.addIceCandidate(new RTCIceCandidate(candidate))
    },

    toggleMicrophone() {
      const audioTracks = this.localStream.getAudioTracks()

      if (audioTracks.length > 0) {
        // Переключаем состояние микрофона
        audioTracks[0].enabled = !audioTracks[0].enabled
        // Обновляем состояние в компоненте
        this.isMicrophoneActive = audioTracks[0].enabled
      }
    },
  },
}
</script>

<style scoped>
.video-container {
  margin: 0 auto;
  margin-top: 1%;
  width: 50%;
  position: relative;
}

.video {
  width: 100%;
  height: auto;
  border: solid white 3px;
  border-radius: 30px;
  transform: scaleX(-1);
}

.remote-video {
  position: absolute; /* Позиционируем удаленное видео поверх локального */
  top: 10px; /* Отступ сверху */
  left: 10px; /* Отступ слева */
  width: 30%; /* Ширина удаленного видео */
  height: auto; /* Автоматическая высота для сохранения пропорций */
}

.button-container {
  display: flex; /* Используем flexbox для расположения кнопок в ряд */
  justify-content: center; /* Центрируем кнопки по горизонтали */
  position: absolute; /* Абсолютное позиционирование для размещения кнопок */
  bottom: 10px; /* Расположение кнопок от нижней границы контейнера */
  left: 50%; /* Центрируем кнопки по горизонтали */
  transform: translateX(-50%);
}

.button-container button {
  margin: 0 5px; /* Отступы между кнопками */
  padding: 4%;
  max-width: 30%;
}
</style>

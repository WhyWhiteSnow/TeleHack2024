<template>
  <div class="header">
    <div class="page-title">
      <p class="header-icon"><font-awesome-icon icon="fa-solid fa-circle" size="lg" /></p>
      <h1>Авторизация</h1>
    </div>
    <company-info class="comp-inf"></company-info>
  </div>
  <div class="container">
    <transition name="slide-fade" mode="out-in">
      <div class="swap" v-if="isTerminal === true">
        <default-button class="selected-form">Авторизация Терминала</default-button>
        <default-button class="btn" @click="switchForm"> Авторизовать Оператора </default-button>
      </div>
      <div class="swap" v-else-if="isTerminal === false">
        <default-button class="btn" @click="switchForm">Авторизовать Терминал</default-button>
        <default-button class="selected-form">Авторизация Оператора</default-button>
      </div>
    </transition>
    <transition name="slide-fade" mode="out-in">
      <terminal-authorisation v-if="isTerminal === true"></terminal-authorisation>
      <support-authorisation v-else></support-authorisation>
    </transition>
  </div>
</template>

<script>
import TerminalAuthorisation from '@/components/TerminalAuthorisation.vue'
import SupportAuthorisation from '@/components/SupportAuthorisation.vue'

export default {
  components: {
    TerminalAuthorisation,
    SupportAuthorisation,
  },
  data() {
    return {
      isTerminal: true,
    }
  },
  methods: {
    switchForm() {
      this.isTerminal = !this.isTerminal
    },
  },
}
</script>

<style scoped>
.header {
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  display: flex;
  color: rgb(07, 01, 23);
  background-color: white;
  padding: 1%;
  align-items: center;
  justify-content: space-around;
}
.page-title {
  display: flex;
  align-items: center;
}
.comp-inf {
  padding-left: 25%;
}
.container {
  height: 100%;
}
.header-icon {
  padding-right: 3%;
}
.swap {
  margin: 1% 0;
  display: flex;
  justify-content: center;
}
.selected-form {
  margin: 0 2%;
  background-color: white;
  color: rgb(07, 01, 23);
  height: 50px;
}
.btn {
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  max-width: 200px;
  padding: 0 1%;
  height: 50px;
}
.btn:active {
  background-color: rgb(07, 01, 23);
  color: white;
}
.slide-fade-enter-active {
  transition: all 0.3s ease-in;
}

.slide-fade-leave-active {
  transition: all 0.3s cubic-bezier(1, 0.5, 0.8, 1);
}

.slide-fade-enter-from,
.slide-fade-leave-to {
  transform: translateX(20px);
  opacity: 0;
}
</style>

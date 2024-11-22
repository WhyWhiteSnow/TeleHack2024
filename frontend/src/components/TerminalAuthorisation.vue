<template>
  <div class="term-auth">
    <form @submit.prevent="submit">
      <p>
        <id-input
          v-model="id"
          id="id"
          name="id"
          class="id"
          placeholder="Укажите id терминала"
          required
        />
      </p>
      <p class="pass-input">
        <pass-input
          v-model="password"
          required
          id="password"
          name="password"
          class="password"
          :type="passwordFieldType"
        />
        <default-button @click="switchVisibility" class="show">
          <span v-if="passwordFieldType === 'password'">
            <font-awesome-icon icon="fa-solid fa-eye" fa="lg" />
          </span>
          <span v-else-if="passwordFieldType === 'text'">
            <font-awesome-icon icon="fa-solid fa-eye-slash" fa="lg" />
          </span>
        </default-button>
      </p>
      <default-button class="btn-subm" @click="$router.push('/terminal')"> Авторизоваться </default-button>
    </form>
  </div>
</template>

<script>

export default {
  name: 'term_auth',
  data() {
    return {
      id: undefined,
      password: '',
      passwordFieldType: 'password',
      token: null,
      errorMessage: '',
    }
  },
  methods: {
    // switchVisibility() {
    //   this.passwordFieldType = this.passwordFieldType === 'password' ? 'text' : 'password'
    // },
    // async submit() {
    //   try {
    //     const response = await axios.post('http://127.0.0.1:8000/autoriseTerminal', {
    //       'id': this.id,
    //       'password': this.password,
    //     })

    //     // Store the token in localStorage or Vuex
    //     this.token = response.data.token // Assuming the token is returned in response.data.token
    //     localStorage.setItem('jwt_token', this.token) // Store token for future requests

    //     // Redirect to terminal page
    //     this.$router.push('/terminal')
    //   } catch (error) {
    //     this.errorMessage = error.response?.data?.message || 'Ошибка авторизации'
    //     console.error(error)
    //   }
    // },
  },
}
</script>

<style scoped>
.term-auth {
  animation-name: auth-page;
  animation-duration: 2s;
  text-align: center;
}
.id {
  max-width: 400px;
}
.pass-input {
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
}
.password {
  margin: 2% 0;
  max-width: 400px;
}
.show {
  background: none;
  border: none;
  padding: 1% 3% 1% 1%;
  margin: 2% 0;
  width: 35px;
  position: absolute;
  right: 35%;
}
.show:active {
  background-color: rgb(07, 01, 23);
  color: white;
  border: solid 3px white;
  border-left: none;
}
.btn-subm {
  max-width: 200px;
  height: 50px;
}
</style>

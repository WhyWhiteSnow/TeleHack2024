<template>
  <div class="supp-auth">
    <form @submit.prevent>
      <p><id-input id="id" name="id" class="id" placeholder="Укажите логин преподавателя" /></p>
      <p class="pass-input">
        <pass-input
          id="password"
          name="password"
          class="password"
          :type="passwordFieldType"
          v-model="password"
        />
        <default-button @click="switchVisibility" class="show">
          <span v-if="passwordFieldType === 'password'">
            <font-awesome-icon icon="fa-solid fa-eye" fa="xl" />
          </span>
          <span v-else-if="passwordFieldType === 'text'">
            <font-awesome-icon icon="fa-solid fa-eye-slash" fa="xl" />
          </span>
        </default-button>
      </p>
      <default-button class="btn-subm" @click="$router.push('/support')">
        Авторизоваться
      </default-button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'term_auth',
  data() {
    return {
      passwordFieldType: 'password',
    }
  },
  methods: {
    switchVisibility() {
      this.passwordFieldType = this.passwordFieldType === 'password' ? 'text' : 'password'
    },
  },
}
</script>

<style scoped>
.supp-auth {
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
  margin: 1% 0;
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

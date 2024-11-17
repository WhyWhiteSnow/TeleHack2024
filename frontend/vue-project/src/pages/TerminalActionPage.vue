<template>
  <div class="container">
    <full-header></full-header>
    <div class="actions">
      <default-button class="btn" title="Заявка на обратный звонок" @click="$router.push('/call')">
        <bold>Заявка на обратный звонок</bold>
      </default-button>
      <br />
      <default-button class="btn" title="Заявка на подключение" @click="$router.push('/connect')">
        <bold>Заявка на подключение</bold>
      </default-button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      terminals: {
        id: '',
        password: '',
      },
    }
  },
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Zen+Dots&display=swap');

.actions {
  margin: 2%;
  text-align: center;
}
.btn {
  height: 70px;
  max-width: 800px;
  margin: 2%;
}
.lock,
.shield {
  padding-right: 3px;
}
</style>

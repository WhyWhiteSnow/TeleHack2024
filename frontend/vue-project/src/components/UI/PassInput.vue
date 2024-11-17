<template>
  <input
    type="password"
    required
    placeholder="Введите пароль"
    title="Введите пароль терминала"
    v-model="password"
  />
</template>

<script>
export default {
  name: 'pass-input',
  data() {
    return {
      password: '',
    }
  },
}
</script>

<style scoped>
input {
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  font-size: larger;
  width: 100%;
  padding: 1%;
  background-color: rgb(07, 01, 23);
  color: white;
  border: solid white 3px;
  border-radius: 50px;
  background-clip: padding-box;
  outline: none;
}
input::placeholder {
  font-size: large;
}
</style>

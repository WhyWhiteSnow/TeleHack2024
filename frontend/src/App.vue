<template>
  <div class="app">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  data() {
    return {
      terminals: { id: '', password: '' },
      supports: { id: '', password: '' },
      application: {
        activity: '',
        surname: '',
        name: '',
        patronymic: '',
        address: '',
        phone: '',
        email: '',
        connectionDate: '',
      },
    }
  },
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
body {
  color: white;
  background-color: rgb(07, 01, 23);
}
</style>

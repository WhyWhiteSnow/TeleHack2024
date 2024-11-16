<template>
  <div class="container">
    <div class="header">
      <div class="activity-icons">
        <p><font-awesome-icon icon="fa-solid fa-globe" fixed-width /></p>
        <p><font-awesome-icon icon="fa-solid fa-tv" fixed-width /></p>
        <p><font-awesome-icon icon="fa-solid fa-video" fixed-width /></p>
        <p class="lock"><font-awesome-icon icon="fa-solid fa-lock" /></p>
        <p class="shield"><font-awesome-icon icon="fa-solid fa-shield-halved" /></p>
      </div>
      <div class="activity-types">
        <p>Интернет</p>
        <p>Телевидение</p>
        <p>Видеонаблюдение</p>
        <p>Домофон</p>
        <p>Системы безопасности</p>
      </div>
      <company-info></company-info>
    </div>
    <div class="actions">
      <default-button class="btn" title="Заявка на обратный звонок">
        <bold>Заявка на обратный звонок</bold>
      </default-button>
      <br />
      <default-button class="btn" title="Заявка на подключение">
        <bold>Заявка на подключение</bold>
      </default-button>
    </div>
  </div>
</template>

<script>
export default {}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Zen+Dots&display=swap');

.header {
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  background-color: white;
  color: rgb(07, 01, 23);
  display: flex;
  padding: 2% 0 2% 7%;
}
.activity-icons {
  margin-right: 1%;
  padding: 0;
  text-align: center;
}
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

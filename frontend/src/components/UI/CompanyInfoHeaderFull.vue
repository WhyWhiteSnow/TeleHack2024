<template>
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
</template>

<script>
export default {
  name: 'full-header',
}
</script>

<style>
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
</style>

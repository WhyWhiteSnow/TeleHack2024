<template>
  <div class="header">
    <div class="activity">
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
    </div>
    <div class="company-contacts">
      <div class="company-title">
        <img
          src="../../img/logo3.png"
          alt="Логотип компании"
          class="base-logo"
          height="70px"
          width="90px"
        />
        Sevencom
      </div>
      <div class="website">sevencom.ru</div>
      <div class="phone">8 909 700-88-77</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'full-header',
}
</script>

<style scoped>
.header {
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  background-color: white;
  color: rgb(07, 01, 23);
  padding: 1% 0;
  display: flex;
  justify-content: space-around;
}
.activity {
  display: flex;
}
.activity-icons {
  margin-right: 3%;
  padding: 0;
  text-align: center;
}
.base {
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  margin: 0 auto;
}
.company-title {
  font-family: 'Zen Dots';
  font-size: xx-large;
  font-weight: bold;
  display: flex;
  align-items: center;
}
.website,
.phone {
  font-size: larger;
  margin-left: 90px;
}
</style>

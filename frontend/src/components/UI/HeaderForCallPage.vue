<template>
  <div class="header">
    <div class="header-name">
      <font-awesome-icon class="header-icon" icon="fa-regular fa-comments" size="2xl" />
      <h1>Видезвонок</h1>
    </div>
    <div class="comp-title">
      <img
        src="../../img/logo3.png"
        alt="Логотип компании"
        class="base-logo"
        height="70px"
        width="90px"
      />
      Sevencom
    </div>
  </div>
</template>

<script>
export default {
  name: 'call-header',
}
</script>

<style scoped>
.header {
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  padding: 1%;
  display: flex;
  justify-content: space-around;
  align-items: center;
  background-color: white;
  color: rgb(07, 01, 23);
}
.header-name {
  display: flex;
}
.header-icon {
  padding-right: 3%;
}
.comp-title {
  font-family: 'Zen Dots';
  font-size: xx-large;
  font-weight: bold;
  display: flex;
  align-items: center;
}
</style>

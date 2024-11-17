<template>
  <div class="header">
    <div class="page-title">
      <font-awesome-icon icon="fa-regular fa-envelope" class="header-icon" size="2xl" />
      <h1>Заявка на подключение</h1>
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
  name: 'conn-header',
}
</script>

<style scoped>
.header {
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  display: flex;
  color: rgb(07, 01, 23);
  background-color: white;
  align-items: center;
  justify-content: space-around;
  padding: 1%;
}
h1 {
  min-width: 100%;
}
.page-title {
  display: flex;
  align-items: center;
}
.header-icon {
  padding-right: 3%;
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

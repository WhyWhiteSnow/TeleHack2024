<template>
  <div class="header">
    <font-awesome-icon icon="fa-regular fa-envelope" class="header-icon" size="2xl" />
    <h1>Заявка на подключение</h1>
    <company-info class="comp-inf"></company-info>
  </div>
</template>

<script>
export default {
  name: 'conn-header',
}
</script>

<style>
.header {
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  display: flex;
  color: rgb(07, 01, 23);
  background-color: white;

  align-items: center;
  justify-content: space-around;
}
.comp-inf {
  padding-left: 25%;
}
.header-icon {
  font-weight: bold;
  padding-right: 1%;
}
</style>

<template>
  <div class="base">
    <div class="company">
      <img
        src="../../img/logo_uisi.jpg"
        alt="Логотип учебного заведения"
        class="base-logo"
        height="70px"
        width="90px"
      />
      UISI
    </div>
    <div class="website">uisi.ru</div>
    <div class="phone">+7 952 512-25-52</div>
  </div>
</template>

<script>
export default {
  name: 'company-info',
}
</script>

<style scoped>
.base {
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  justify-content: space-around;
}
.company img {
  margin-right: 3%;
}
.company {
  font-family: 'Zen Dots';
  font-size: xx-large;
  font-weight: bold;
  display: flex;
  align-items: center;
}
.website,
.phone {
  font-size: larger;
  margin-left: 100px;
}
</style>

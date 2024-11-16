<template>
  <div class="base">
    <div class="company">
      <img
        src="../../img/logo3.png"
        alt="Логотип компании"
        class="base-logo"
        height="70px"
        width="70px"
      />
      <h1>Sevencom</h1>
    </div>
    <div class="website">sevencom.ru</div>
    <div class="phone">8 909 700-88-77</div>
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
  margin: 0 auto;
}
.company {
  font-family: 'Zen Dots';
  display: flex;
  align-items: center;
}
.website,
.phone {
  font-size: larger;
  margin-left: 75px;
}
</style>

<template>
  <button class="btn">
    <slot></slot>
  </button>
</template>

<script>
export default {
  name: 'default-button',
}
</script>

<style scoped>
.btn {
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  width: 100%;
  background-color: rgb(07, 01, 23);
  color: white;
  border: solid blue 2px;
  border-radius: 50px;
  font-size: large;
  cursor: pointer;
}
.btn:active {
  background-color: white;
  color: rgb(07, 01, 23);
  border: solid blue 3px;
}
@media (pointer: coarse) {
  button:hover {
    background-color: rgb(07, 01, 23);
    color: white;
  }
}
</style>

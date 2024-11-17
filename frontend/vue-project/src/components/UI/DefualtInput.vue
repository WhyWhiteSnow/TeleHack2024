<template>
  <input type="text" required />
</template>

<script>
export default {
  name: 'def-input',
}
</script>

<style>
input {
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  font-size: larger;
  width: 100%;
  padding: 1%;
  background-color: rgb(07, 01, 23);
  color: white;
  border: solid white 3px;
  border-radius: 50px;
  outline: none;
}
input::placeholder {
  font-size: large;
}
</style>

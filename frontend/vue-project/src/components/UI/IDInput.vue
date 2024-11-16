<template>
    <input
    type="number" 
    required 
    min="1"
    max="100" 
    placeholder="Укажите id" 
    autofocus 
    title="Укажите id терминала" 
    />
</template>

<script>
    export default {
        name: "id-input"
        
    }
</script>

<style scoped>
    input {
        font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
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
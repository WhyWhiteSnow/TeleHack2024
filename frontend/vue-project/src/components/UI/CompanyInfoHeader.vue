<template>
    <div class="base">
        <div class="company">
            <img src="../../img/" alt="Логотип компании" class="base-logo">
            <h1>Sevencom</h1>
        </div>
        <div class="website">
            sevencom.ru
        </div>
        <div class="phone">
            8 909 700-88-77
        </div>
    </div>
</template>

<script>
    export default {
        name: "company-info"
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
    }
    .website, .phone {
        font-size: larger;
        padding-top: 5px;
        margin-left: 145px;
    }
</style>
<template>
    <div>
        <div class="container">
            <div class="terminals">
                <div class="terminal">
                    <img src="../img/dbfd3008248fa7f133395b3e8a4faa6b.jpg" alt="Видео с терминала" height="200px">
                    <div class="name">Терминал 1</div>
                    <div class="address">
                        г. Полевской, ул. Победы, 7
                    </div>
                    <div class="status">
                        <font-awesome-icon icon="fa-solid fa-user" />
                        <div>Свободен</div>
                    </div>
                </div>
                <div class="terminal">
                    <img src="../img/c5lSG2srXc4.jpg" alt="Видео с терминала">
                    <div class="name">Терминал 2</div>
                    <div class="address">
                        г. Среднеуральск, ул. Строителей, 8А
                    </div>
                    <div class="status">
                        <font-awesome-icon icon="fa-solid fa-user" />
                        <div>Свободен</div>
                    </div>
                </div>
                <div class="terminal">
                    <img src="../img/photo_2024-10-03_14-57-21.jpg" alt="Видео с терминала">
                    <div class="name">Терминал 3</div>
                    <div class="address">
                        г. Талица, ул. Луначарского, 69А оф. 66
                    </div>
                    <div class="status">
                        <font-awesome-icon icon="fa-solid fa-user" />
                        <div>Свободен</div>
                    </div>
                </div>
                <div class="terminal">
                    <img src="../img/scale_1200.jpeg" alt="Видео с терминала">
                    <div class="name">Терминал 4</div>
                    <div class="address">
                        г. Полевской, ул. Коммунистическая, 29
                    </div>
                    <div class="status">
                        <font-awesome-icon icon="fa-solid fa-user" />
                        <div>Свободен</div>
                    </div>
                </div>
                <div class="terminal">
                    <img src="../img/c5lSG2srXc4.jpg" alt="Видео с терминала">
                    <div class="name">Терминал 2</div>
                    <div class="address">
                        г. Среднеуральск, ул. Строителей, 8А
                    </div>
                    <div class="status">
                        <font-awesome-icon icon="fa-solid fa-user" />
                        <div>Свободен</div>
                    </div>
                </div>
                <div class="terminal">
                    <img src="../img/c5lSG2srXc4.jpg" alt="Видео с терминала">
                    <div class="name">Терминал 2</div>
                    <div class="address">
                        г. Среднеуральск, ул. Строителей, 8А
                    </div>
                    <div class="status">
                        <font-awesome-icon icon="fa-solid fa-user" />
                        <div>Свободен</div>
                    </div>
                </div>
                <div class="terminal">
                    <img src="../img/c5lSG2srXc4.jpg" alt="Видео с терминала">
                    <div class="name">Терминал 2</div>
                    <div class="address">
                        г. Среднеуральск, ул. Строителей, 8А
                    </div>
                    <div class="status">
                        <font-awesome-icon icon="fa-solid fa-user" />
                        <div>Свободен</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {

    }
</script>

<style>
    .container {
        font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
        height: 100vh;
    }
    .terminals {
        padding-top: 1%;
        color: rgb(07, 01, 23);
        display: flex;
        flex-wrap: wrap;
        width: 100%;
    }
    .terminal {
        border: solid 3px lightgray;
        margin: 5px;
        width: 19%;
        background-color: white;
        height: 50vh;
        position: relative;
    }
    .terminal img {
        width: 100%;
        height: 50%;
    }
    .name {
        font-size: large;
        font-weight: bold;
        margin: 3% 5% 2%;
    }
    .address {
        display: flex;
        padding: 0 5%;
        margin-bottom: 5%;
    }
    .status {
        display: flex;
        background-color: lightgray;
        position: absolute;
        width: 100%;
        height: 15%;
        padding-left: 5%;
        align-items: center;
        bottom: 0;
    }
    .status div {
        padding-left: 2%;
        font-size: large;
    }
</style>
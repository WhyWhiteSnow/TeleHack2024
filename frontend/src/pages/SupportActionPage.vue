<template>
  <div>
    <div class="container">
      <div class="terminals" v-for="terminal in terminals">
        <div class="terminal" @click="$router.push('/call')">
          <img :src="terminal.imgSrc" alt="Видео с терминала" title="Видео с терминала" />
          <div class="name">{{ terminal.name }}</div>
          <div class="address">{{ terminal.address }}</div>
          <div class="status">
            <font-awesome-icon icon="fa-solid fa-user" />
            <div>{{ terminal.status }}</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      terminals: [
        {
          id: 1,
          imgSrc: 'src/img/dbfd3008248fa7f133395b3e8a4faa6b.jpg',
          name: 'Терминал 1',
          address: 'г. Полевской, ул. Победы, 7',
          status: 'Свободен',
        },
        {
          id: 2,
          name: 'Терминал 2',
          imgSrc: 'src/img/c5lSG2srXc4.jpg',
          address: 'г. Среднеуральск, ул. Строителей, 8А',
          status: 'Свободен',
        },
        {
          id: 3,
          name: 'Терминал 3',
          imgSrc: 'src/img/photo_2024-10-03_14-57-21.jpg',
          address: 'г. Талица, ул. Луначарского, 69А оф. 66',
          status: 'Свободен',
        },
        {
          id: 4,
          name: 'Терминал 4',
          imgSrc: 'src/img/scale_1200.jpeg',
          address: 'г. Полевской, ул. К. Маркса, 9А',
          status: 'Свободен',
        },
        {
          id: 5,
          name: 'Терминал 5',
          imgSrc: 'src/img/photo_2024-10-03_14-57-27.jpg',
          address: 'г. Верхняя Пышма, Успенский проспект, 127',
          status: 'Свободен',
        },
        {
          id: 6,
          name: 'Терминал 6',
          imgSrc:
            'src/img/141936-goku-risovanie-shar_drakona-vymyslennyj_personaz-illustracia-7680x4320.jpg',
          address: 'г. Полевской, ул. Победы, 7',
          status: 'Свободен',
        },
      ],
    }
  },
}
</script>

<style scoped>
.container {
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  height: 100vh;
  display: flex;
  flex-wrap: wrap;
}
.terminals {
  color: rgb(07, 01, 23);
  width: 20%;
}
.terminal {
  cursor: pointer;
  border: solid 3px lightgray;
  margin: 5px;
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

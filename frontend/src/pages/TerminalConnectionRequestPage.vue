<template>
  <conn-header></conn-header>
  <div class="container">
    <form class="conn-form" @submit.prevent="submitForm">
      <div class="select">
        <label for="activity">ВЫБЕРИТЕ УСЛУГУ</label>
        <select name="activity" id="activity" v-model="application.activity">
          <option value="TV">Телевидение</option>
          <option value="internet">Интернет</option>
          <option value="cctv">Видеонаблюдение</option>
          <option value="intercom">Домофон</option>
        </select>
      </div>
      <p>Заполните формы</p>
      <div class="person-name">
        <def-input
          v-model="application.surname"
          class="input"
          maxlength="30"
          placeholder="Введите Фамилию"
          title="Введите фамилию"
        />
        <def-input
          v-model="name"
          class="input"
          maxlength="30"
          placeholder="Введите Имя"
          title="Введите имя"
        />
        <def-input
          v-model="patronymic"
          class="input"
          maxlength="30"
          placeholder="Введите Отчество"
          title="Введите отчество"
        />
      </div>
      <div class="person-contacts">
        <def-input
          v-model="address"
          class="input"
          maxlength="30"
          placeholder="Введите Адрес проживания (улица и дом)"
          title="Введите адрес проживания"
        />
        <def-input
          v-model="phone"
          class="input"
          type="phone"
          placeholder="Введите Номер телефона"
          title="Введите номер телефона"
        />
        <def-input
          v-model="email"
          class="input"
          type="email"
          placeholder="Введите Адрес электронной почты"
          title="Введите адрес электронной почты"
        />
      </div>
      <div class="date">
        <label for="date">Выберите дату для подключения услуги</label>
        <def-input
          v-model="connectionDate"
          class="input input-date"
          :min="today"
          type="date"
          placeholder="Введите дату"
          title="Введите дату"
          id="date"
        />
      </div>
      <def-input class="submit" type="submit" value="Отправить Заявку" />
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      today: new Date().toISOString().split('T')[0],
      application: {
        activity: '',
        surname: '',
        name: '',
        patronymic: '',
        address: '',
        phone: '',
        email: '',
        connectionDate: '',
      },
    }
  },
  methods: {
    submitForm() {
      // Здесь можно обработать отправку формы
      console.log({
        activity: this.activity,
        surname: this.surname,
        name: this.name,
        patronymic: this.patronymic,
        address: this.address,
        phone: this.phone,
        email: this.email,
        connectionDate: this.connectionDate,
      })
    },
  },
}
</script>

<style scoped>
.conn-form {
  margin: 1%;
}
.select {
  border-radius: 50px;
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  font-size: x-large;
  font-weight: bolder;
  display: flex;
  align-items: center;
  flex-direction: column;
  margin: 0 auto;
}
select {
  font-size: medium;
  background-color: rgb(07, 01, 23);
  color: white;
  border-radius: 2em;
  border: 3px solid white;
  margin-top: 1%;
  width: 200px;
  height: 50px;
  padding: 1%;
}
.input {
  margin-bottom: 1%;
  max-width: 400px;
}
p {
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  font-size: x-large;
  margin-left: 3%;
}
.person-name {
  margin-top: 1%;
  display: flex;
  justify-content: space-around;
}
.person-contacts {
  display: flex;
  justify-content: space-around;
}
.date {
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  font-size: larger;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.input-date {
  font-size: medium;
  margin-top: 1%;
  color: white;
  width: 200px;
  margin-bottom: 0;
}
.submit {
  width: 200px;
  float: right;
  margin-right: 2%;
}
</style>

<template>
  <section>
    <Header />
    <NavBar />
    <h2>Здравствуйте, {{ profileInfo.name }}!</h2>
    <button class="red-button1" @click="logOut">Выйти</button>
    <p>
      Вид абонемента: полный<br>
      Дней до конца абонемента: 265<br>
      Последнее посещение: 29.10.2020
    </p>
    <img class="avatar" src="./../assets/avatar.png" alt="avatar">
    <div v-for="booking in bookingList" v-bind:key="booking.id">
      <p><strong>{{ booking.lesson_type.name }}</strong><br>
        {{ booking.time.slice(0,5) }} {{ booking.weekday }}<br>
        {{ booking.coach.name }}<br>
        <button class="red-button1" @click="deleteBooking(booking.id)">Удалить</button></p>
    </div>
    <Footer />
  </section>
</template>

<script>
import $ from 'jquery'
import Header from '@/components/Header'
import NavBar from '@/components/NavBar'
import Footer from '@/components/Footer'

export default {
  name: 'Home',

  metaInfo: {
    title: 'Личный кабинет',
    meta: [{
      name: 'viewport',
      content: 'width=device-width, initial-scale=1'
    }]
  },
  components: {
    Header,
    NavBar,
    Footer
  },
  data: () => ({
    profileInfo: [],
    bookingList: [],
    weekdays: {
      Mon: 'Понедельник',
      Tue: 'Вторник',
      Wen: 'Среда',
      Thu: 'Четверг',
      Fri: 'Пятница',
      Sat: 'Суббота',
      Sun: 'Воскресенье'
    }
  }),
  created () {
    $.ajaxSetup({
      headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
    })
    this.loadBookings()
  },
  methods: {
    loadBookings () {
      $.ajax({
        url: 'http://127.0.0.1:8000/profile/',
        type: 'GET',
        success: (response) => {
          this.profileInfo = response['0']
          this.bookingList = response['0'].bookings
        }
      })
    },
    deleteBooking (id) {
      $.ajax({
        url: `http://127.0.0.1:8000/book/${id}/delete`,
        type: 'DELETE',
        success: (response) => {
          alert(response)
          location.reload()
        }
      })
    },
    logOut () {
    }
  }
}
</script>

<style>
p, h2 {
  text-align: center;
  margin-top: 10px;
}
.red-button1 {
  background-color: red;
  color: white;
  padding: 0 10px 0 10px;
  border-radius: 10px;
  border: none;
  margin-top: 10px;
  margin-bottom: 10px;
}
.avatar {
  width: 30%;
  margin-bottom: 10px;
}
</style>

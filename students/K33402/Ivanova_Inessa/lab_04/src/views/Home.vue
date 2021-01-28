<template>
  <section>
    <Header />
    <NavBar />
    <h2>Здравствуйте, {{ profileInfo.name }}!</h2>
    <button class="offset-lg-9" @click="logOut">Выйти</button>
    <div class="row">
      <div class="col-lg-3 offset-lg-4">
        <img class="avatar" src="./../assets/avatar.png" alt="avatar">
      </div>
      <div class="info col-lg-2"><p>
        Данные пользователя<br>
        Телефон: {{ profileInfo.tel }} <br>
        Рост: {{ profileInfo.height }} <br>
        Вес: {{ profileInfo.weight }} <br> </p>
        <div>
          <button
            id="app"
            type="button"
            @click="showModal"
          >
            Изменить
          </button>

          <ProfileInfo
            v-show="isModalVisible"
            @close="closeModal"
            :tel="profileInfo.tel"
            :height="profileInfo.height"
            :weight="profileInfo.weight"
          />
        </div>
      </div>
    </div>
    <div v-for="booking in bookingList" v-bind:key="booking.id" class="list">
      <p><strong>{{ booking.lesson_type.name }}</strong><br>
        {{ booking.time.slice(0,5) }} {{ weekdays[booking.weekday] }}<br>
        {{ booking.coach.name }}<br>
        <button type="button" @click="deleteBooking(booking.id)">Удалить</button></p>
    </div>
    <Footer />
  </section>
</template>

<script>
import $ from 'jquery'
import Header from '@/components/Header'
import NavBar from '@/components/NavBar'
import Footer from '@/components/Footer'
import ProfileInfo from '@/components/ProfileInfo'

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
    Footer,
    ProfileInfo
  },
  data: () => ({
    profileInfo: [],
    bookingList: [],
    isModalVisible: false,
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
    this.getProfileInfo()
    this.loadBookings()
  },
  methods: {
    showModal () {
      this.isModalVisible = true
    },
    closeModal () {
      this.isModalVisible = false
    },
    /**
     * Функиця получает информацию о пользователе в переменную this.profileInfo
     */
    getProfileInfo () {
      $.ajax({
        url: 'http://127.0.0.1:8000/auth/users/me',
        type: 'GET',
        success: (response) => {
          this.profileInfo = response
          console.log(response)
        }
      })
    },
    /**
     * Функиця подгружает занятия, на которые записан пользователь в переменную this.bookingList
     */
    loadBookings () {
      $.ajax({
        url: 'http://127.0.0.1:8000/profile/',
        type: 'GET',
        success: (response) => {
          this.bookingList = response['0'].bookings
          console.log(response)
        }
      })
    },
    /**
     * Функция удаляет запись на занятие
     * @param {number} a
     */
    deleteBooking (a) {
      $.ajax({
        url: `http://127.0.0.1:8000/book/${a}/delete`,
        type: 'DELETE',
        success: (response) => {
          alert(response)
          location.reload()
        }
      })
    },
    /**
     * Функция для выхода из аккаунта, удаляет токен из sessionStorage
     */
    logOut () {
      sessionStorage.removeItem('auth_token')
      this.$router.push('login')
    }
  }
}
</script>

<style>
h2 {
  text-align: center;
  margin-top: 10px;
}
.info {
  text-align: left;
  margin-top: 10px;
}
.list {
  text-align: center;
  margin-top: 10px;
}
.avatar {
  width: 100%;
  margin-bottom: 10px;
}
</style>

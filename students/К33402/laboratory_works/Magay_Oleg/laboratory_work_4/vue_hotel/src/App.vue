<template>
  <v-app>
    <v-app-bar app dark>
      <div class="d-flex align-center">
        <h1 class="headline">Название отеля</h1>
        <v-row v-if='isAuth'>
          <v-col class="col"><router-link class="route" to="/">Главная</router-link></v-col>
          <v-col class="col"><router-link class="route" to="/room">Номера</router-link></v-col>
          <v-col class="col"><router-link class="route" to="/staff">Персонал</router-link></v-col>
          <v-col class="col"><router-link class="route" to="/profile">Профиль</router-link></v-col>
          <v-col class="col"><a class="a-route" @click="logout">Выход</a></v-col>
        </v-row>
        <v-row v-if='!isAuth'>
          <v-col class="col"><router-link class="route" to="/login">Вход</router-link></v-col>
          <v-col class="col"><router-link class="route" to="/register">Регистрация</router-link></v-col>
        </v-row>
      </div>
    </v-app-bar>

    <v-main class="my-5 px-5">
      <router-view />
    </v-main>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  data: () => ({
    isAuth: ''
  }),
  created () {
    this.isAuth = localStorage.getItem('token') !== null && localStorage.getItem('token') !== undefined
    if (localStorage.getItem('token')) {
      this.axios.defaults.headers.common.Authorization = `Token ${localStorage.getItem('token')}`
    }
    console.log(this.isAuth, localStorage.getItem('token'), this.axios.defaults.headers.common.Authorization)
  },
  methods: {
    logout () {
      localStorage.removeItem('token')
      delete this.axios.defaults.headers.common.Authorization
      window.location.href = 'http://localhost:8080/login/'
    }
  }
}
</script>

<style scoped>
  .headline {
    margin:20px;
  }
  .col {
    margin:20px;
    color: white;
  }
  .route {
    color: white;
  }
  .a-route {
    color: white;
    text-decoration: underline;
    object-position: right;
  }
</style>

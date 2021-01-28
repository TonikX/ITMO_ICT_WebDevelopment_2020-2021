<template>
  <div>
    <div v-if="auth">
      <v-app-bar color="#653d19" dense dark>
        <v-toolbar-title>Arthub</v-toolbar-title>
        <v-btn class="ma-2" outlined color="white" @click="goAuthorlist">Лист авторов</v-btn>
        <v-spacer></v-spacer>
        <v-btn icon @click="goLK">
          <v-icon>mdi-account</v-icon>
        </v-btn>
        <v-btn icon @click="logout">
          <v-icon>mdi-exit-to-app</v-icon>
        </v-btn>
      </v-app-bar>
    </div>
    <div class="block-content">
      <div v-if="!auth">
        <div class="label">Arthub</div>
        <div class="description">Какую кнопку выберешь ты?</div>
        <v-btn class="button" depressed color="primary" @click="goLogin">Войти</v-btn>
        <v-btn class="button" depressed color="error" @click="goRegistration">Регистрация</v-btn>
      </div>
      <div v-if="auth">
        <Creationlist></Creationlist>
      </div>

    </div>
  </div>

</template>

<script>
// @ is an alias to /src
import Creationlist from '@/components/Creationlist.vue'
export default {
  name: 'Home',
  components: {
    Creationlist
  },
  computed: {
    auth () {
      if (sessionStorage.getItem('auth_token')) {
        return true
      }
      return false
    }
  },
  methods: {
    goLogin () {
      this.$router.push({ name: 'Login' })
    },
    logout () {
      sessionStorage.removeItem('auth_token')
      window.location = '/home'
    },
    goRegistration () {
      this.$router.push({ name: 'Signin' })
    },
    goLK () {
      this.$router.push({ name: 'LK' })
    },
    goAuthorlist () {
      this.$router.push({ name: 'Authorlist' })
    }
  }
}
</script>
<style>
.block-content {
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: space-around;
  background: #fff0b5; /* Цвет фона */
  padding: 10px; /* Поля вокруг текста */
}
.label{
  margin: auto;
  text-decoration: none;
  font-family: 'Lora', serif;
  font-style: normal;
  text-align: center;
  transition: .5s linear;
  width: 276px;
  font-size: 60px;
}
.description{
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 14px;
  text-decoration: none;
  font-family: 'Lora', serif;
  font-style: normal;
  text-align: center;
  transition: .5s linear;
  width: 252px;
  font-size:20px;
}
.button{
  width:150px;
  margin: 10px;
}
</style>

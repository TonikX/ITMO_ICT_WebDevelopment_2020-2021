<template>

  <v-main>
    <header-component />
    <v-row id="auth-form">
      <v-col cols="4" class="mx-auto" id="auth-block">
        <v-card>
        <v-card-title id="color_">Вход</v-card-title>
        <v-card-text id="space" v-if="!error">
          <v-form class="my-0" id="space2" @submit="signIn" ref="form">
            <v-text-field label="Username" v-model="username"></v-text-field>
            <v-text-field label="Password" v-model="password" type="password"></v-text-field>
            <v-btn dark type="submit" color="#008EAB" class="mx-0 my-4" id="enter" width="100px">Войти</v-btn>
          </v-form>
        </v-card-text>
        <v-card-text id="space" v-else>
          <v-form class="my-0" id="space2" @submit="signIn">
            <p id="error">Неверный логин или пароль</p>
            <v-text-field label="Username" v-model="username"></v-text-field>
            <v-text-field label="Password" v-model="password" type="password"></v-text-field>
            <v-btn dark type="submit" color="#008EAB" class="mx-0 my-4" id="enter" width="100px">Войти</v-btn>
          </v-form>
        </v-card-text>
    </v-card>
      </v-col>
    </v-row>

  </v-main>
</template>

<script>
import HeaderComponent from '../components/Header'
const host = 'http://127.0.0.1:8000/api/'

export default {
  name: 'Auth',
  components: { HeaderComponent },
  created () {
    if (localStorage.getItem('token')) {
      this.$router.push('/')
    }
  },
  data: () => ({
    username: null,
    password: null,
    error: false,
    savedUserName: null
  }),
  methods: {
    /**
     * Отправляет запрос на авторизацию
     * @param event
     */
    signIn (event) {
      event.preventDefault()
      this.axios.post(host + 'auth/token/login/',
        { username: this.username, password: this.password })
        .then(response => { this.setLogined(response.data.auth_token) })
        .catch(_ => {
          this.error = true
        })
      this.savedUserName = this.username
      this.$refs.form.reset()
    },
    /**
     * Устанваливает юзернэйм и токен в локальное хранилище и
     * @param token
     */
    setLogined (token) {
      localStorage.setItem('token', token)
      localStorage.setItem('username', this.savedUserName)
      this.$router.push('/')
    }
  }
}
</script>

<style scoped>
  #auth-form{
    margin-top: 5%;

  }

  #auth-block {
    min-width: 400px;
    max-width: 800px;
  }

  .primary{
    color: white;
  }

  #space {
    padding-bottom: 0px;
  }

  #space2 {
    padding-top: 20px;
  }

  #enter {
    height: 40px;
  }

  #error {
    font-size: 17px;
    text-align: center;
    padding-top: 8px;
    background-color: darkred;
    height: 40px;
    color: white;
  }

  #color_ {
    background-color: #005B7C;
    color: white;
  }
  main{
    background-color: #EFEFEE;
  }

</style>

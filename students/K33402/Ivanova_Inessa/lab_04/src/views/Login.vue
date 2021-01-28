<template>
  <section>
    <Header />
    <NavBar />
    <div class="login">
      <h2>Войти в личный кабинет</h2>
      <div>
        <input v-model="login" class="window" type="text" placeholder="Введите логин" />
      </div>
      <div>
        <input v-model="password" class="window" type="password" placeholder="Введите пароль" />
      </div>
      <button class="red-button1" @click="setLogin">Войти</button>
    </div>
    <Footer />
  </section>
</template>

<script>
import Header from '@/components/Header'
import NavBar from '@/components/NavBar'
import Footer from '@/components/Footer'
import $ from 'jquery'

export default {
  name: 'Login',

  metaInfo: {
    title: 'Вход',
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
    login: '',
    password: ''
  }),
  methods: {
    /**
     * Функция получает токен с заданными логином и паролем
     */
    setLogin () {
      $.ajax({
        url: 'http://127.0.0.1:8000/auth/token/login/',
        type: 'POST',
        data: {
          username: this.login,
          password: this.password
        },
        success: (response) => {
          alert('Вы успешно вошли')
          sessionStorage.setItem('auth_token', response.auth_token)
          this.$router.push('home')
        },
        error: (response) => {
          if (response.status === 400) {
            alert('Неверный логин или пароль')
          }
        }
      })
    }
  }
}
</script>

<style>
.red-button1 {
  background-color: red;
  color: white;
  padding: 5px 30px 5px 30px;
  border-radius: 10px;
  border: none;
}
.window {
  margin: 10px;
  width: 300px
}
h1 {
  text-align: center;
}
.login {
  margin-top: 15px;
  height: 600px;
}
</style>

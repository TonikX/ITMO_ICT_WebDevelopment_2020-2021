<template>
  <div>
    <input v-model="login" type="text" placeholder="Логин"/>
    <input v-model="password" type="password" placeholder="Пароль"/> <br/>
    <button @click="setLogin">Войти</button> <br/>
    <button @click="createUser">Зарегистрироваться</button> <br/>

  </div>
</template>

<script>
import $ from 'jquery'

export default {

  name: 'login',
  data () {
    return {
      login: '',
      password: ''
    }
  },
  created () {
    $.ajaxSetup({
      headers: {}
    })
  },
  methods: {
    /**
     * Function for auth user
     */
    setLogin () {
      $.ajax({
        url: 'http://127.0.0.1:8005/auth/token/login/',
        type: 'POST',
        data: {
          username: this.login,
          password: this.password
        },
        success: (response) => {
          console.log(response.auth_token)
          sessionStorage.setItem('auth_token', response.auth_token)
          this.$router.push({ name: 'ChooseInterface' })
        },
        error: (response) => {
          if (response.status === 400) {
            alert('Неверный логин или пароль')
          }
          console.log(response)
        }
      })
    },
    createUser () {
      $.ajax({
        url: 'http://127.0.0.1:8005/auth/users/',
        type: 'POST',
        data: {
          username: this.login,
          password: this.password
        },
        success: (response) => {
          alert('Регистрация прошла успешно')
        },
        error: (response) => {
          alert(response.responseText + '\n' + response.statusText)
        }
      })
    }
  }
}
</script>

<style scoped>

</style>

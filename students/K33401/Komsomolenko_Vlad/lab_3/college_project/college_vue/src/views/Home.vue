<template>
  <v-main class="d-flex align-center text-center">
    <v-col v-if='auth'>
      <h1 class="headline">Добро пожаловать!</h1>
    </v-col>
    <v-col v-if='!auth'>
      <h1 class="headline">Вы не вошли в свой аккаунт.</h1>
      <p class="mt-5"><router-link to="/login">Войти</router-link></p>
    </v-col>
    <router-view />
  </v-main>
  </template>
<script>

export default {
  name: 'Home',
  computed: {
    auth () {
      if (localStorage.getItem('auth_token')) {
        return true
      }
      return false
    }
  }
}
</script>

<style scoped>
</style>

<template>
  <v-app>
    <v-app-bar
      app
      color="orange"
      light
    >
      <div class="d-flex align-items-center">
        <h1 class="black-05">Poultry Farm Service</h1>
    <v-btn>
      <router-link to="/chickenslist">Chickens</router-link>
    </v-btn>

    <v-btn>
      <router-link to="/breedslist">Breeds</router-link>
    </v-btn>

    <v-btn>
      <router-link to="/cellslist">Cells</router-link>
    </v-btn>

    <v-btn>
      <router-link to="/profile">Profile</router-link>
    </v-btn>
      </div>
    </v-app-bar>

    <v-main class="my-5 px-5">
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
import $ from 'jquery'
export default {
  name: 'App',
  created () {
    if (localStorage.getItem('token')) {
      $.ajaxSetup({
        headers: {
          Authorization: 'Token' + localStorage.getItem('token')
        }
      })
    }
  }
}
</script>

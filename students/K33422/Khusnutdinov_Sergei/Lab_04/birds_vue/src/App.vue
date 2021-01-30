<template>
  <v-app>
    <v-app-bar
      app
      color="gray"
      dark
    >
      <div class="d-flex align-center">
        <h1 class="headline"> Birds Project </h1>
        <v-icon>mdi-dragon</v-icon>
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
      <router-link to="/settings">Settings</router-link>
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

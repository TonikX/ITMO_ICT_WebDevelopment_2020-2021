<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      light
    >
      <div class="d-flex align-center">
        <h1 class="headline">Poultry Farm</h1>
    <v-btn>
      <router-link to="/chickenslist">Chickens</router-link>
      <v-icon>mdi-bird</v-icon>
    </v-btn>

    <v-btn>
      <router-link to="/breedslist">Breeds</router-link>
      <v-icon>mdi-eye</v-icon>
    </v-btn>

    <v-btn>
      <router-link to="/cellslist">Cells</router-link>
      <v-icon>mdi-map-marker</v-icon>
    </v-btn>

    <v-btn>
      <router-link to="/settings">Settings</router-link>
      <v-icon>mdi-wrench</v-icon>
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

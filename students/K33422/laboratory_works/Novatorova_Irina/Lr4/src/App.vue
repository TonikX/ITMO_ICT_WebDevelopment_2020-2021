<template>
  <v-app>
    <v-app-bar
      app
      color="pink accent-1"
      light
    >
      <div class="d-flex align-center">
        <h1 class="headline">Luch Marketing Agency</h1>
        <v-divider
      class="mx-5"
      vertical
    ></v-divider>
        <v-btn text href="/">Home</v-btn>
        <v-divider
      class="mx-5"
      vertical
    ></v-divider>
        <v-btn text href="/application">Applications</v-btn>
        <v-divider
      class="mx-5"
      vertical
    ></v-divider>
        <v-btn text href="/client">Clients</v-btn>
        <v-divider
      class="mx-5"
      vertical
    ></v-divider>
        <v-btn text href="/materials">Materials</v-btn>
        <v-divider
      class="mx-5"
      vertical
    ></v-divider>
        <v-btn text href="/services">Services</v-btn>
        <v-divider
      class="mx-5"
      vertical
    ></v-divider>
        <v-btn text href="/worker">Workers</v-btn>
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

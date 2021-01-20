<template>
  <v-app>
    <v-app-bar
      app
      color="pink darken-3"
      dark
    >
      <v-toolbar-title>College system</v-toolbar-title>

      <v-divider
      class="mx-4"
      vertical
    ></v-divider>

      <v-btn text href="/">Home</v-btn>

      <v-btn text href="/about">About</v-btn>

      <v-btn  v-if='auth'
              text href="/profile">Profile</v-btn>

      <v-spacer></v-spacer>

      <v-btn v-if='auth'
             class="ma-2"
             dark
             @click="logOut">
        <v-icon
          dark
          left> mdi-login</v-icon>Logout</v-btn>

      <v-btn v-if='!auth'
             class="ma-2"
             dark
             href="/signin">
        <v-icon
          dark
          left> mdi-login</v-icon>Login</v-btn>

      <v-btn v-if='!auth'
             class="ma-2"
             dark
             href="/signup">
        <v-icon
          dark
          left> mdi-account-box</v-icon>Register</v-btn>
    </v-app-bar>

    <v-main class="my-5 px-5">
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'App',

  computed: {
    auth () {
      if (localStorage.getItem('token')) {
        return true
      } else {
        return false
      }
    }
  },

  methods: {
    logOut () {
      localStorage.removeItem('token')
      localStorage.removeItem('role')
      localStorage.removeItem('username')
      this.$router.push('/')
      this.$router.go()
    }
  }
}
</script>

<template>
  <v-app>
    <div>
      <v-toolbar dense
                 dark
                 color="#252526"
      >

        <v-toolbar-title @click="goToHome" style="cursor: pointer">Отель</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-toolbar-items class="hidden-sm-and-down">
          <v-btn color="#white" plain @click="goToRooms">
            Номера
          </v-btn>
          <v-btn color="#white" plain @click="goToGuests">
            Посетители
          </v-btn>
        </v-toolbar-items>
        <v-btn icon @click="logout">
          <v-icon>mdi-export</v-icon>
        </v-btn>
      </v-toolbar>
    </div>
    <v-main>
      <v-container fluid>
        <router-view></router-view>
      </v-container>
    </v-main>
  </v-app>

</template>

<script>
export default {
  name: 'App',
  data: () => ({}),
  methods: {
    logout () {
      localStorage.removeItem('auth_token')
      this.$router.push({ name: 'Login' })
    },
    goToGuests () {
      this.$router.push({ name: 'Guests' })
    },
    goToRooms () {
      this.$router.push({ name: 'Rooms' })
    },
    goToHome () {
      this.$router.push({ name: 'Home' })
    }
  }
}

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  text-align: center;
  color: #D5D3D0;
}
.ttxt{
  margin-top: 2%;
  font-size: 150%;
}
</style>

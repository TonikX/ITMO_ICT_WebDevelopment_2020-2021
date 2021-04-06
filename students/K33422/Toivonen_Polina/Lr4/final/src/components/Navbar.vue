<template>
  <nav>
    <v-toolbar class="light-blue lighten-5">
      <v-toolbar-title>
        <span class="black--text">Medical Clinic</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn
        v-for="item in menu"
        :key="item"
        :to="item.link"
        class="v-toolbar--flat black--text green darken-4"
      >
        <span class="font-weight-bold">{{ item.label }}</span>
      </v-btn>
    </v-toolbar>
  </nav>
</template>

<script>
export default {
  name: 'Navbar',
  data: () => ({
    menu: []
  }),
  methods: {
    getMenu () {
      if (this.isLogged()) {
        this.menu = [
          {
            label: 'Home',
            link: '/'
          },
          {
            label: 'Profile',
            link: '/personalpage'
          },
          {
            label: 'Services',
            link: '/price'
          },
          {
            label: 'Cabinets',
            link: '/cabinet'
          },
          {
            label: 'Patients',
            link: '/patient'
          },
          {
            label: 'Diagnosis',
            link: '/diagnosis'
          },
          {
            label: 'Logout',
            link: '/logout'
          }
        ]
      } else {
        this.menu = [
          {
            label: 'Home',
            link: '/'
          },
          {
            label: 'Login',
            link: '/login'
          },
          {
            label: 'Signup',
            link: '/register'
          }
        ]
      }
      return this.menu
    },
    isLogged () {
      const token = localStorage.getItem('token')
      return !!token
    }
  },
  created () {
    this.getMenu()
    this.$bus.$on('logged', () => {
      this.getMenu()
    })
  }
}
</script>

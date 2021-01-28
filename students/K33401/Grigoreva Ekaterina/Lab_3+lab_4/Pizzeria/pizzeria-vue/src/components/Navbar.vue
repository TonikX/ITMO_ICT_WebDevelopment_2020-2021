<template>
  <nav>
    <v-toolbar class="orange">
      <v-toolbar-title>
        <span class="white--text">Pizza</span>
        <span class="font-weight-bold brown--text">4U</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn
        v-for="item in menu"
        :key="item"
        :to="item.link"
        class="v-toolbar--flat white--text orange"
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
            label: 'Personal Page',
            link: '/personalpage'
          },
          {
            label: 'Pizzas',
            link: '/pizza'
          },
          {
            label: 'SignOut',
            link: '/signout'
          }
        ]
      } else {
        this.menu = [
          {
            label: 'Home',
            link: '/'
          },
          {
            label: 'SignIn',
            link: '/signin'
          },
          {
            label: 'SignUp',
            link: '/signup'
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

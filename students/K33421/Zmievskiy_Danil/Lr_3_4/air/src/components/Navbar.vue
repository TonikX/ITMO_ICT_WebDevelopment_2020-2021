<template>
  <nav>
    <v-toolbar class="teal lighten-3">
      <v-toolbar-title>
        <span class="black--text">Аэропорт</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn
        v-for="item in menu"
        :key="item"
        :to="item.link"
        class="v-toolbar--flat black--text teal accent-2"
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
            label: 'Моя Страница',
            link: '/personalpage'
          },
          {
            label: 'Экипаж',
            link: '/ekipazh'
          },
          {
            label: 'Самолеты',
            link: '/planes'
          },
          {
            label: 'Рейсы',
            link: '/reys'
          },
          {
            label: 'Транзит',
            link: '/tranzit'
          },
          {
            label: 'Выйти',
            link: '/signout'
          }
        ]
      } else {
        this.menu = [
          {
            label: 'Главная',
            link: '/'
          },
          {
            label: 'Войти',
            link: '/login'
          },
          {
            label: 'Зарегестрироваться',
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

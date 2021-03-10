<template>
  <nav>
    <v-toolbar class="deep-purple">
      <v-toolbar-title>
        <span class="white--text">Лечебная клиника</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn
        v-for="item in menu"
        :key="item"
        :to="item.link"
        class="v-toolbar--flat white--text pink darken-4"
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
            label: 'Главная',
            link: '/'
          },
          {
            label: 'Профиль',
            link: '/personalpage'
          },
          {
            label: 'Пациенты',
            link: '/patient'
          },
          {
            label: 'Кабинеты',
            link: '/cabinet'
          },
          {
            label: 'Услуги',
            link: '/price'
          },
          {
            label: 'База диагнозов',
            link: '/diagnosis'
          },
          {
            label: 'Выйти из аккаунта',
            link: '/logout'
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
            label: 'Регистрация',
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

<template>
  <v-card
    flat
    tile
  >
    <v-toolbar dense
               dark
               color="primary"
    >
      <v-toolbar-title @click="goToHome" style="cursor: pointer">Opros.ru</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items v-if="isLogged" class="hidden-sm-and-down">
        <v-btn color="white" plain @click="goToProfile">
          Личный кабинет
        </v-btn>
        <v-btn color="white" plain @click="logout">
          Выйти
        </v-btn>
      </v-toolbar-items>
      <v-toolbar-items v-else>
        <v-btn color="white" plain @click="login">
          Войти
        </v-btn>
      </v-toolbar-items>
    </v-toolbar>
  </v-card>
</template>

<script>
import { TOKEN_KEY } from '../../variables'

export default {
  name: 'Toolbar',
  props: {
    isLogged: Boolean
  },
  methods: {
    /**
     * Выход из учетной записи
     */
    logout () {
      sessionStorage.removeItem(TOKEN_KEY)
      this.$forceUpdate()
      this.isLogged = false
      this.emitEventChanged()
    },
    /**
     * Вход в учетную запись
     */
    login () {
      this.$router.push({ name: 'SignIn' })
    },
    /**
     * Открытие профиля
     */
    goToProfile () {
      this.$router.push({ name: 'Profile' })
    },
    /**
     * Переход на главную страницу
     */
    goToHome () {
      if (this.$router.currentRoute.path !== '/polls') {
        this.$router.push({ name: 'Home', params: { isHome: true } }).catch(() => {})
      }
    },
    /**
     * Отправляет событие смены флага
     */
    emitEventChanged () {
      this.$emit('IsLoggedChanged', this.isLogged)
    }
  }
}
</script>

<style scoped>

</style>

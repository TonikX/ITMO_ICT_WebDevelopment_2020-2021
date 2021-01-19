<template>
  <v-app>
    <v-app-bar
      app
      color="black"
      dark
    >
      <div class="d-flex align-center">
        <h1 class="headline">Komsomolenko</h1>
      </div>
      <v-spacer></v-spacer>

      <v-btn
        v-if='auth'
        href="/students"
        text
      >
        <span class="mr-2">Ученики</span>
      </v-btn>
      <v-btn
        v-if='auth'
        href="/teachers"
        text
      >
        <span class="mr-2">Преподователи</span>
      </v-btn>
      <v-btn
        v-if='auth'
        href="/marks"
        text
      >
        <span class="mr-2">Оценки</span>
      </v-btn>
      <v-btn
        v-if='auth'
        href="/subjects"
        text
      >
        <span class="mr-2">Предметы и расписания</span>
      </v-btn>
      <v-btn
        v-if='!auth'
        href="/login"
        text
      >
        <span class="mr-2">Войти</span>
      </v-btn>
      <v-btn
        v-if='auth'
        @click='disconnect'
        text
      >
        <span class="mr-2">Выйти</span>
      </v-btn>
    </v-app-bar>
    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>

export default {
  name: 'App',
  created () {
    if (localStorage.getItem('auth_token')) {
      this.axios.defaults.headers.common.Authorization = `Token ${localStorage.getItem('auth_token')}`
    }
  },
  computed: {
    auth () {
      console.log(localStorage.getItem('auth_token'))
      if (localStorage.getItem('auth_token')) {
        return true
      }
      return false
    }
  },
  methods: {
    async disconnect () {
      console.log(localStorage.getItem('auth_token'))
      localStorage.removeItem('auth_token')
      console.log(localStorage.getItem('auth_token'))
      delete this.axios.defaults.headers.common.Authorization
      window.location.href = '/'
    }
  }
}
</script>

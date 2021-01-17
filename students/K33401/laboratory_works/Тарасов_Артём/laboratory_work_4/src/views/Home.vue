<template>
  <div class="home">
    <Login v-if="auth"/>
    <Books v-if="!auth"/>
  </div>
</template>

<script>
// @ is an alias to /src
import Books from '@/components/Books'
import Login from '@/components/Login'

export default {
  name: 'home',
  components: {
    Login,
    Books
  },
  methods: {
    auth (login) {
      if (sessionStorage.getItem('auth_token') && login) {
        return true
      }
      return false
    }
  }
}
</script>

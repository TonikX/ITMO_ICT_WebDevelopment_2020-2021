<template>
  <div class="home">
    <Login v-if="auth"/>
    <ChooseInterface v-if="!auth"/>
  </div>
</template>

<script>
// @ is an alias to /src
import Login from '@/components/Login'
import ChooseInterface from '@/components/ChooseInterface'

export default {
  name: 'home',
  components: {
    ChooseInterface,
    Login
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

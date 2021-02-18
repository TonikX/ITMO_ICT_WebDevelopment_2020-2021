<template>
  <div class="home">
    <h1>Welcome,
    <span v-if="auth">{{ userData.username }}</span>
    <span v-else>Guest</span>!
  </h1>
    <br>
    <span v-if="!auth" style="color: #AD1457">You're not signed in.</span>

    <v-col class="ma-auto" v-if="isDis">
      <nav-menu-dis class />
    </v-col>

    <v-col class="ma-auto" v-if="isTeacher">
      <nav-menu-te class />
    </v-col>

    <v-col class="ma-auto" v-if="isStudent">
      <nav-menu-st class />
    </v-col>
  </div>
</template>

<script>
import NavMenuDis from '@/components/NavMenuDis.vue'
import NavMenuTe from '@/components/NavMenuTe.vue'
import NavMenuSt from '@/components/NavMenuSt.vue'

export default {
  components: { NavMenuDis, NavMenuTe, NavMenuSt },
  name: 'Home',

  data: () => ({
    userData: {
    }
  }),

  created () {
    this.loadUserData()
  },

  computed: {

    auth () {
      if (localStorage.getItem('token')) {
        return true
      } else {
        return false
      }
    },

    isStudent () {
      if (localStorage.getItem('role') === 's') {
        return true
      } else {
        return false
      }
    },

    isTeacher () {
      if (localStorage.getItem('role') === 't') {
        return true
      } else {
        return false
      }
    },

    isDis () {
      if (localStorage.getItem('role') === 'd') {
        return true
      } else {
        return false
      }
    }
  },

  methods: {
    async loadUserData () {
      try {
        const response = await this.axios
          .get('http://localhost:8000/auth/users/me/', {
            headers: {
              Authorization: `Token ${localStorage.getItem('token')}`
            }
          })

        // if (response.status !== 200) {
        //   throw new Error(response.status)
        // }
        this.userData = response.data
        localStorage.setItem('role', this.userData.role)
        localStorage.setItem('username', this.userData.username)
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    }
  }
}

</script>

<style>
form {
  display: flex;
}

.form-group {
  display: flex;
  flex-direction: column;
  width: 25%;
  text-align: left;
  gap: 0.5rem;
  margin: auto;
  margin-top: 2rem
}
</style>

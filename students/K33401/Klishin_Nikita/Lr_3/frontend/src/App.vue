<template>
  <v-app>
    <v-app-bar dark app fixed>
      <v-toolbar-title>
        <router-link to="/" tag="span">
          PEER SYSTEM
        </router-link>
      </v-toolbar-title>
      
      <v-spacer></v-spacer>

      <v-toolbar-items>
        <v-btn text
          v-for="item in menuItems"
          :key="item.title"
          :to="item.path">
          <v-icon left dark>{{ item.icon }}</v-icon>
          {{ item.title }}
        </v-btn>
      </v-toolbar-items>

      <v-spacer></v-spacer>
      
      <v-toolbar-items class="hidden-xs-only">
        <v-btn text
          v-for="item in autoriztionLinks"
          :key="item.title"
          :to="item.path">
          <v-icon left dark>{{ item.icon }}</v-icon>
          {{ item.title }}
        </v-btn>
      </v-toolbar-items>
    </v-app-bar>

    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>


export default {
  name: 'App',
  components: {
  },

  computed: {
    authenticated() {
      return this.$store.getters.IS_AUTHENTICATED
    }
  },
  data() {
    return {
      token: null,
      menuItems: [
        { title: 'Tasks', path: '/tasks', icon: 'task_alt' },
        { title: 'Add', path: '/add', icon: 'add_task' },
        { title: 'Classes', path: '/classes', icon: 'dns' },
        { title: 'Criterions', path: '/criterions', icon: 'spellcheck' }
      ],
      autoriztionLinks: null
    }
  },
  watch: {
    authenticated(value) {
      console.log("Watch:" + value)
      this.changeLinks(value)
    }
  },
  mounted() {
    this.changeLinks(this.authenticated)

    if (localStorage.getItem('token') !== null) { // если token существует в локальном хранилище
      // TODO
    }
    
  },
  methods: {
    changeLinks(isAuthenticated) {
      if (isAuthenticated) {
        this.autoriztionLinks = [
          { title: 'Profile', path: '/profile', icon: 'home' },
          { title: 'Logout', path: '/logout', icon: 'exit_to_app' }
        ]
      } else {
        this.autoriztionLinks = [
          { title:  'Sign In', path: '/login', icon: 'login'},
          { title: 'Sign Up', path: '/register', icon: 'how_to_reg' }
        ]
      }
    }
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #000000;
}

.darken {
  color: aliceblue;
}

.mydark {
        background: #000000;
        color: aliceblue;
    }
</style>

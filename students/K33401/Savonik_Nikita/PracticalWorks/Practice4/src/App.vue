<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex align-center">
        <h1 class="headline">Простой проект на Vue</h1>
      </div>

    </v-app-bar>
    <v-main class="d-flex text-center">
      <nav>
        <router-link to="/" class="link">Home</router-link> |
        <router-link to="/nasa" class="link">Nasa</router-link>
      </nav>
      <router-view />
    </v-main>

  </v-app>
</template>

<script>
export default {
  name: 'App',

  data: () => ({
    //
  })
}
</script>
<style>
nav {
 padding: 30px;
}

nav .link {
 font-weight: bold;
 color: white;
 text-decoration: none;
}

nav .link.router-link-exact-active {
 color: #42b983;
}
</style>

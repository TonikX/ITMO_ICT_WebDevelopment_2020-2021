<template>
  <v-app
    color="background">
    <v-main>
        <router-view/>
    </v-main>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  data: () => ({
    isLogged: Boolean
  })
}
</script>

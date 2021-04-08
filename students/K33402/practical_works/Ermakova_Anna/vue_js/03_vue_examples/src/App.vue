<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <div className="d-flex align-center">
        <h1 className="headline">Простой проект на Vue</h1>
      </div>
    </v-app-bar>

    <v-main className="d-flex align-center text-center">
      <router-view/>
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

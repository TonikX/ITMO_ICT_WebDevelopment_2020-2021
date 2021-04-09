<template>
    <v-app>
    <router-view />
    <footer-part />
  </v-app>
</template>

<script>

import FooterPart from './components/Footer'
export default {
  name: 'App',
  components: { FooterPart }
}
</script>

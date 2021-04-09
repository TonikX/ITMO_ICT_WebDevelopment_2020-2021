<template>
   <v-footer padless id="footer-background">
    <v-col
      class="text-center"
      cols="12"
      id = "footer-text"
    >
      {{ new Date().getFullYear() }} — <strong>Fluffy Friend</strong>
    </v-col>
  </v-footer>
</template>

<script>
export default {
  name: 'FooterPart'
}
</script>

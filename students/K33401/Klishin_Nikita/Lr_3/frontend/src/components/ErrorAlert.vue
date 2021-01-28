<template>
  <div>
    <v-alert v-if="message" class="text-center" dense outlined type="error" max-width="700px">
      {{ message }}
    </v-alert>
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: null,
    }
  }
}
//:value="message"
</script>

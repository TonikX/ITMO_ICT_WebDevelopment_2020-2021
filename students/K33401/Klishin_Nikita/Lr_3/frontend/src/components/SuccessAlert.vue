<template>
  <div>
    <v-alert v-if="message" class="text-center" dense outlined type="success" max-width="700px">
      {{ message }}
    </v-alert>
  </div>
</template>

<script>
export default {
  props: {
    message: String,
  },
  data() {
    return {
      // message: null,
    }
  }
}
//:value="message"
</script>
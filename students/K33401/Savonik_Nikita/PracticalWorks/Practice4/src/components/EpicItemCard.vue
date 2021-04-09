<template>

  <v-row>
    <v-col cols="10" class="mx-auto">
      <v-card
  elevation="3"
  class="px-6 py-6 my-4"
  color="#EFEFEE"
  >
    <v-row >
      <v-col cols="6">
        <v-img :src="epicItem.image" />
      </v-col>
      <v-col cols="6">
        <v-card-text class="text-left py-0 px-0">
          {{ epicItem.caption }}
        </v-card-text>
      </v-col>
    </v-row>
  </v-card>
    </v-col>
  </v-row>
</template>

<script>
export default {
  name: 'EpicItemCard',
  props: {
    epicItem: Object
  }
}
</script>

<style scoped>
</style>

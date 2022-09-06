<template>

  <v-row>
    <v-col cols="10" class="mx-auto">
      <v-card
        min-height="400px"
        max-height="400px"
  elevation="3"
  class="px-3 py-3 my-4"
  >
    <v-row style="min-height: 400px; max-height: 400px">
      <v-col cols="6" style="background: #EFEFEE" class="px-0 py-0">
        <v-img v-if="cat.pic" :src="cat.pic" height="100%" width="100%" />
        <v-img v-else :src="'https://img5.goodfon.ru/wallpaper/nbig/0/c8/kotik-kotenok-fon.jpg'" height="100%" width="100%" />
      </v-col>
      <v-col cols="6" class="px-6" style="background: #EFEFEE">
        <v-card-title class="py-0" id="name">{{ cat.name }}</v-card-title>
        <v-divider class="my-1"></v-divider>
        <v-card-text class="text-left py-4 px-0" id="text">
          <p><b> Порода </b>: {{ cat.breed }} <br></p>
          <p><b> Цена </b>: {{cat.price}}<br></p>
          {{ cat.description }}
          <v-divider class="my-2"></v-divider>
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
    cat: Object
  }
}
</script>

<style scoped>
  #name {
    padding: 0;
    font-size: 23px;
  }
  #text {
    font-size: 17px;
  }
</style>

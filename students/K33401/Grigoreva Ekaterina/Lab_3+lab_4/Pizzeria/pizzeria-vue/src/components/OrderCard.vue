<template>
  <v-card
    elevation="2"
    class="px-2 py-3"
  >
    <v-row>
      <v-col cols="2" class="py-0">
        <v-card-title class="py-auto fill-height">
          {{ orderItem.id }}
        </v-card-title>
      </v-col>
      <v-col cols="10">
        <v-row>
          <v-col cols="8" class="py-0">
            <v-card-text class="brown--text font-weight-bold text-capitalize">
              Type of pizza
            </v-card-text>
          </v-col>
          <v-col cols="4" class="py-0">
            <v-card-text class="brown--text font-weight-bold text-capitalize">
              Price
            </v-card-text>
          </v-col>
        </v-row>
        <v-row
          v-for="pizza in orderItem.pizzas"
          :key="pizza.id"
        >
          <v-col cols="8" class="py-3">
            <v-card-text>
              {{ pizza.name }}
            </v-card-text>
          </v-col>
          <v-col cols="4" class="py-3">
            <v-card-text>
              {{ pizza.price }}
            </v-card-text>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </v-card>
</template>

<script>
export default {
  name: 'OrderCard',

  props: {
    orderItem: Object
  }
}
</script>

<style scoped>

</style>

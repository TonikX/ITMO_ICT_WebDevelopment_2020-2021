<template>
  <v-card
    elevation="2"
    class="px-2 py-5"
  >
    <v-row>
      <v-col cols="3">
        <v-img src="../assets/pizza.png" />
      </v-col>

      <v-col cols="4">
        <v-card-text class="brown--text font-weight-bold text-capitalize">
          Type of pizza
        </v-card-text>
        <v-card-text>
          {{ pizzaItem.name }}
        </v-card-text>
      </v-col>

      <v-col cols="2">
        <v-card-text class="brown--text font-weight-bold text-capitalize">
          Price
        </v-card-text>
        <v-card-text>
          {{ pizzaItem.price }}
        </v-card-text>
      </v-col>

      <v-col cols="3" class="my-auto">
        <v-btn @click="deletePizza(pizzaItem.id)" class="my-3" style="width: 100px">Delete</v-btn>
        <v-btn @click="changePizza(pizzaItem.id)" class="my-3" style="width: 100px">Change</v-btn>
      </v-col>
    </v-row>
  </v-card>
</template>

<script>
export default {
  name: 'PizzaCard',

  props: {
    pizzaItem: Object
  },

  methods: {
    async deletePizza (pizzaId) {
      try {
        this.token = localStorage.getItem('token')
        if (this.token) {
          this.axios.defaults.headers.common.Authorization = `token ${this.token}`
        }

        await this.axios.delete(`http://127.0.0.1:8000/api/pizzas/${pizzaId}/delete/`)
        this.$bus.$emit('changingPizzas', 'Pizza deleted')
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    changePizza (pizzaId) {
      localStorage.setItem('pizzaId', pizzaId)
      this.$bus.$emit('changeOne', 'Change one pizza')
    }
  }
}
</script>

<style scoped>

</style>

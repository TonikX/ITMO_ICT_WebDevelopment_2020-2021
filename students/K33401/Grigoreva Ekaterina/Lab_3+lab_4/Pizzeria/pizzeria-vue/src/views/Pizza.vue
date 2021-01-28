<template>
  <section>
    <v-row>
      <v-col cols="3" class="mt-5">
        <v-form
          @submit.prevent="addPizza"
          ref="pizzaForm"
          class="my-2"
        >
          <v-row>
            <v-col cols="9" class="mx-auto">
              <v-text-field
                label="Enter type of pizza"
                v-model="pizzaForm.name"
              />
              <v-text-field
                label="Enter price of pizza"
                v-model="pizzaForm.price"
              />
            </v-col>
          </v-row>
          <v-btn type="submit" color="brown" dark>Add pizza</v-btn>
        </v-form>
      </v-col>
      <v-col cols="6" class="mx-auto">
        <pizza-card
          v-for="pizzaItem in pizzaItems"
          :key="pizzaItem.id"
          :pizza-item="pizzaItem"
          class="my-2"
        />
      </v-col>
      <v-col cols="3" class="mx-auto" v-if="!toChange"></v-col>
      <v-col cols="3" class="mt-5" v-if="toChange">
        <v-form
          @submit.prevent="changePizza"
          ref="pizzaChangeForm"
          class="my-2"
        >
          <v-row>
            <v-col cols="9" class="mx-auto">
              <v-text-field
                label="Enter type of pizza"
                v-model="pizzaChangeForm.name"
              />
              <v-text-field
                label="Enter price of pizza"
                v-model="pizzaChangeForm.price"
              />
            </v-col>
          </v-row>
          <v-btn type="submit" color="brown" dark>Change pizza info</v-btn>
        </v-form>
      </v-col>
    </v-row>
  </section>
</template>

<script>
import PizzaCard from '../components/PizzaCard.vue'
const host = 'http://127.0.0.1:8000/'

export default {
  name: 'Pizza',

  components: { PizzaCard },

  data: () => ({
    pizzaItems: [],
    token: '',
    pizzaForm: {
      name: '',
      price: 0
    },
    pizzaChangeForm: {
      name: '',
      price: 0
    },
    toChange: false
  }),

  methods: {
    async getPizzaItems () {
      try {
        this.token = localStorage.getItem('token')
        if (this.token) {
          this.axios.defaults.headers.common.Authorization = `token ${this.token}`
        }

        const response = await this.axios
          .get(`${host}api/pizzas/`)

        if (response.status !== 200) {
          throw new Error(response.error)
        }

        console.log(response.data)

        this.pizzaItems = response.data.map((pizzaItem) => {
          console.log(pizzaItem)
          return pizzaItem
        }).reverse()
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    addPizza () {
      try {
        this.token = localStorage.getItem('token')
        if (this.token) {
          this.axios.defaults.headers.common.Authorization = `token ${this.token}`
        }
        const response = this.axios
          .post(`${host}api/pizzas/create/`, this.pizzaForm)
          .then(info => {
            this.$bus.$emit('changingPizzas', 'Pizza added')
            this.$refs.pizzaForm.reset()
          })
        if (response.status !== 201) {
          throw new Error(response.status)
        }
        this.$refs.pizzaForm.reset()
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },

    openChangeForm () {
      this.toChange = true
    },

    changePizza () {
      try {
        this.token = localStorage.getItem('token')
        if (this.token) {
          this.axios.defaults.headers.common.Authorization = `token ${this.token}`
        }
        const pizzaId = localStorage.getItem('pizzaId')
        const response = this.axios
          .patch(`${host}api/pizzas/${pizzaId}/update/`, this.pizzaChangeForm)
          .then(info => {
            this.$bus.$emit('changingPizzas', 'Pizza changed')
            this.toChange = false
            localStorage.removeItem('pizzaId')
            this.$refs.pizzaChangeForm.reset()
          })
        if (response.status !== 201) {
          throw new Error(response.status)
        }
        this.$refs.pizzaChangeForm.reset()
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    }
  },

  created () {
    this.getPizzaItems()
    this.$bus.$on('changingPizzas', () => {
      this.getPizzaItems()
    })
    this.$bus.$on('changeOne', () => {
      this.openChangeForm()
    })
  }
}
</script>

<style>
</style>

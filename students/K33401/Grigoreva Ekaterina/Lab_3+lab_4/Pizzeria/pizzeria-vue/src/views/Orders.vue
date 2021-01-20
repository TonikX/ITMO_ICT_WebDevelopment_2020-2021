<template>
  <section>
    <v-row>
      <v-col cols="6" class="mx-auto">
        <order-card
          v-for="orderItem in orderItems"
          :key="orderItem.id"
          :order-item="orderItem"
          class="my-2"
        />
      </v-col>
    </v-row>
  </section>
</template>

<script>
import OrderCard from '@/components/OrderCard'
const host = 'http://127.0.0.1:8000/'

export default {
  name: 'Orders',

  components: { OrderCard },

  data: () => ({
    orderItems: [],
    token: ''
  }),

  methods: {
    async getOrderItems () {
      try {
        this.token = localStorage.getItem('token')
        if (this.token) {
          this.axios.defaults.headers.common.Authorization = `token ${this.token}`
        }

        const response = await this.axios
          .get(`${host}api/orders/`)

        if (response.status !== 200) {
          throw new Error(response.error)
        }

        console.log(response.data)

        this.orderItems = response.data.map((orderItem) => {
          console.log(orderItem)
          return orderItem
        })

        // response = await this.axios
        //   .get(`${host}api/orderedPizzas/`)
        //
        // if (response.status !== 200) {
        //   throw new Error(response.error)
        // }
        //
        // for (let item = 0; item < response.data.length; item++) {
        //   console.log(response.data[item])
        // }
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    }
  },

  created () {
    this.getOrderItems()
  }
}
</script>

<style scoped>

</style>

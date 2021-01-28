<template>
  <div>
    <h1 class="brown--text mt-0 pt-0 mb-7">Personal page</h1>
    <v-row>
      <v-col cols="3" class="mx-auto">
        <h3 class="brown--text mt-0 pt-0 mb-7">Personal info</h3>
        <v-card v-if="!change">
          <p class="pt-5"> <b class="brown--text">Username:</b> {{username}} </p>
          <p> <b class="brown--text">First name:</b> {{ userForm.first_name }} </p>
          <p> <b class="brown--text">Last name:</b> {{ userForm.last_name }} </p>
          <p> <b class="brown--text">Date of birth:</b> {{ userForm.date_of_birth }} </p>
          <p class="pb-5"> <b class="brown--text">Address:</b> {{userForm.address}} </p>
        </v-card>
        <v-form
          @submit.prevent="changeUser"
          ref="userForm"
          v-if="change"
        >
          <v-text-field
            label="First name"
            v-model="userForm.first_name"
          />
          <v-text-field
            label="Last name"
            v-model="userForm.last_name"
          />
          <v-text-field
            label="Date of birth"
            v-model="userForm.date_of_birth"
          />
          <v-text-field
            label="Address"
            v-model="userForm.address"
          />
          <v-btn type="submit" color="brown" dark>Submit</v-btn>
        </v-form>
        <v-btn
          @click="openForm()"
          class="my-3"
          style="width: 100px"
          color="brown"
          dark
          v-if="!change"
        >
          Change
        </v-btn>
        <br>
        <v-btn
          @click="showDelete()"
          class="v-list-item--link"
          v-if="!toDelete"
        >
          Delete profile
        </v-btn>
        <v-form
        v-if="toDelete"
        @submit.prevent="deleteUser"
        >
          <v-text-field
            label="Enter password to confirm"
            v-model="password"
            type="password"
          />
          <v-btn type="submit" color="brown" dark>Submit</v-btn>
        </v-form>
      </v-col>
      <v-col cols="6" class="mx-auto">
        <h3 class="brown--text mt-0 pt-0 mb-7">Your orders</h3>
        <order-card
          v-for="orderItem in orderItems"
          :key="orderItem.id"
          :order-item="orderItem"
          class="my-2"
        />
      </v-col>
    </v-row>
  </div>
</template>

<script>
import OrderCard from '@/components/OrderCard'
const host = 'http://127.0.0.1:8000/'

export default {
  name: 'PersonalPage',

  components: { OrderCard },

  data: () => ({
    username: '',
    userForm: {
      date_of_birth: '',
      address: '',
      first_name: '',
      last_name: ''
    },
    change: false,
    orderItems: [],
    toDelete: false,
    password: ''
  }),

  methods: {
    getParametrs () {
      try {
        const token = localStorage.getItem('token')
        if (token) {
          this.axios.defaults.headers.common.Authorization = `token ${token}`
        }
        this.axios
          .get(`${host}auth/users/me/`)
          .then(response => {
            this.username = response.data.username
            this.userForm.first_name = response.data.first_name
            this.userForm.last_name = response.data.last_name
            this.userForm.address = response.data.address
            this.userForm.date_of_birth = response.data.date_of_birth
          })
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },

    openForm () {
      this.change = true
    },

    changeUser () {
      try {
        const token = localStorage.getItem('token')
        if (token) {
          this.axios.defaults.headers.common.Authorization = `token ${token}`
        }
        console.log(this.userForm)
        const response = this.axios
          .patch(`${host}auth/users/me/`, this.userForm)
          .then(resp => {
            this.change = false
            this.getParametrs()
            this.$refs.userForm.reset()
          })
        if (response.status !== 201) {
          throw new Error(response.status)
        }
        this.$refs.userForm.reset()
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },

    async getOrderItems () {
      try {
        const token = localStorage.getItem('token')
        if (token) {
          this.axios.defaults.headers.common.Authorization = `token ${token}`
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
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },

    showDelete () {
      this.toDelete = true
    },

    deleteUser () {
      try {
        const token = localStorage.getItem('token')
        if (token) {
          this.axios.defaults.headers.common.Authorization = `token ${token}`
        }
        console.log(this.password)
        this.axios
          .delete(`${host}auth/users/me/`, { data: { current_password: this.password } })
          .then(resp => {
            this.change = false
            localStorage.removeItem('token')
            this.toDelete = false
            this.$bus.$emit('logged', 'User deleted')
            this.$router.push('/signin')
          })
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    }
  },

  created () {
    this.getParametrs()
    this.getOrderItems()
  }
}
</script>

<style scoped>
  p {
    text-align: left;
    padding-left: 25px;
  }
</style>

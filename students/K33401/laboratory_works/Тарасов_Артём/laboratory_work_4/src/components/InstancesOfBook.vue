<template>
  <div>
    <button @click="getObjects">Получить экземпляры</button>
    <v-simple-table class="v-data-table">
      <template v-slot:default class="theme--light">
        <thead>
        <tr>
          <th class="text-center">
            id
          </th>
          <th class="text-center">
            status
          </th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="object in objects" v-bind:key="object.id">
          <td>
            <router-link :to="{name:'OneInstanceOfBook', params:{id: object.id}}">{{ object.id }}</router-link>
          </td>
          <td>{{ object.status }}</td>
          <td>
            <v-btn color="#ff0000" @click="deleteObject(object.id)">Удалить</v-btn>
          </td>
        </tr>
        </tbody>
        <v-btn @click="createObject">Добавить экземпляр</v-btn>
      </template>
    </v-simple-table>
  </div>
</template>

<script>
import $ from 'jquery'

const baseUrlApi = 'http://127.0.0.1:8005/api/instancesOfBook/'
export default {
  name: 'InstancesOfBook',
  created () {
    $.ajaxSetup({
      headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
    })
    this.getObjects()
  },
  data () {
    return {
      objects: ''
    }
  },
  methods: {
    /**
     * Function for getting all data
     */
    getObjects () {
      $.ajax({
        url: baseUrlApi,
        type: 'GET',
        success: (response) => {
          console.log(response)
          this.objects = response
        },
        error: (response) => {
          alert('Пользователь не авторизован')
          console.log(response)
        }
      })
    },
    /**
     * Function for route to another component
     */
    createObject () {
      this.$router.push({ name: 'OneInstanceOfBook' })
    },

    /**
     * Function for delete data object
     * @param {number} id
     */
    deleteObject (id) {
      $.ajax({
        url: baseUrlApi + id + '/',
        type: 'DELETE',
        success: (response) => {
          alert('Готово')
          console.log(response)
          this.getObjects()
        },
        error: (response) => {
          alert('Пользователь не авторизован')
          console.log(response)
        }
      })
    }
  }

}
</script>

<style scoped>

</style>

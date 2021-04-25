<template>
  <div>
    <button @click="getObjects">Получить данные о выдаче книг</button>
    <v-simple-table class="v-data-table">
      <template v-slot:default class="theme--light">
        <thead>
        <tr>
          <th class="text-center">
            id
          </th>
          <th class="text-center">
            start date
          </th>
          <th class="text-center">
            return date
          </th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="object in objects" v-bind:key="object.id">
          <td>
            <router-link :to="{name:'OneIssuingAInstances', params:{id: object.id}}">{{ object.id }}</router-link>
          </td>
          <td>{{ object.start_date }}</td>
          <td>{{ object.return_date }}</td>
          <td>
            <v-btn color="#ff0000" @click="deleteObject(object.id)">Удалить</v-btn>
          </td>
        </tr>
        </tbody>
        <v-btn @click="createObject">Добавить данные о выдаче книги</v-btn>
      </template>
    </v-simple-table>
  </div>
</template>

<script>
import $ from 'jquery'

const baseUrlApi = 'http://127.0.0.1:8005/api/issuingAInstances/'
export default {
  name: 'IssuingAInstances',
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
      this.$router.push({ name: 'OneIssuingAInstances' })
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

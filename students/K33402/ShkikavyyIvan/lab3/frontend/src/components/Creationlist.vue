<template>
  <div>
    <v-simple-table class="v-data-table">
      <template v-slot:default class="theme--light">
        <thead>
        <tr>
          <th class="text-center">
            Название
          </th>
          <th class="text-center">
            Автор
          </th>
          <th class="text-center">
            Тип произведения
          </th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="creation in creations" v-bind:key="creation.id">
          <td>
            <router-link :to="{name:'Creation', params:{id: creation.id}}">{{ creation.name }}</router-link>
          </td>
          <td>
            <router-link :to="{name:'Author', params:{id: creation.creator.id}}">{{ creation.creator.name }}
            </router-link>
          </td>
          <td>{{ creation.type }}</td>
          <td>
            <v-btn v-if="!isRedactor" v-on:click="goReview(creation.id)">Оставить отзыв</v-btn>
            <v-btn color="error" v-else @click="deleteCreation(creation.id)">Удалить произведение</v-btn>
          </td>
        </tr>
        </tbody>
        <v-btn v-if="isRedactor" v-on:click="goNewCreation">Добавить произведение</v-btn>
      </template>
    </v-simple-table>
  </div>
</template>

<script>
import $ from 'jquery'
export default {
  name: 'Creationlist',
  data () {
    return {
      creations: '',
      isRedactor: false
    }
  },
  created () {
    $.ajaxSetup({
      headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
    })
    this.loadRedactor()
    this.loadCreations()
  },
  methods: {
    loadCreations () {
      $.ajax({
        url: 'http://127.0.0.1:8000/api/creations/',
        type: 'GET',
        success: (response) => {
          this.creations = response
        },
        error: (response) => {
          alert(response)
        }
      })
    },
    goReview (creationId) {
      this.$router.push({ name: 'Review', params: { creationId: creationId } })
    },
    goNewCreation () {
      this.$router.push({ name: 'NewCreation' })
    },
    loadRedactor () {
      $.ajax({
        url: 'http://127.0.0.1:8000/api/isRedactor/',
        type: 'GET',
        success: (response) => {
          this.isRedactor = Boolean(response)
        },
        error: (response) => {
          alert(response)
        }
      })
    },
    deleteCreation (creationId) {
      $.ajax({
        url: 'http://127.0.0.1:8000/api/creations/' + creationId + '/delete/',
        type: 'DELETE',
        success: (response) => {
          alert('Запись удалена')
          this.loadCreations()
        },
        error: (response) => {
          alert(response)
        }
      })
    }
  }
}
</script>

<style scoped>
.v-data-table {
  line-height: 5;
  width: 1200px;
  max-width: 100%;
}
.theme--light.v-data-table{
  background-color: #FFD7A7;
}
</style>

<template>
  <div>
    <button @click="getBooks">Получить книги</button>
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
        <tr v-for="book in books" v-bind:key="book.id">
          <td>
            <router-link :to="{name:'OneBook', params:{id: book.id}}">{{ book.name }}</router-link>
          </td>
          <td>
            {{ book.author }}
          </td>
          <td>{{ book.section }}</td>
          <td>
            <v-btn color="#ff0000" @click="deleteBook(book.id)">Удалить</v-btn>
          </td>
        </tr>
        </tbody>
        <v-btn @click="createBook">Добавить книгу</v-btn>
      </template>
    </v-simple-table>
  </div>
</template>

<script>
import $ from 'jquery'

export default {
  name: 'Books',
  created () {
    $.ajaxSetup({
      headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
    })
  },
  data () {
    return {
      books: ''
    }
  },
  methods: {
    getBooks () {
      $.ajax({
        url: 'http://127.0.0.1:8005/api/books/',
        type: 'GET',
        success: (response) => {
          console.log(response)
          this.books = response
        },
        error: (response) => {
          alert('Пользователь не авторизован')
          console.log(response)
        }
      })
    },
    createBook () {
      this.$router.push({ name: 'CreateBook' })
    },
    deleteBook (id) {
      $.ajax({
        url: 'http://127.0.0.1:8005/api/books/' + id + '/',
        type: 'DELETE',
        success: (response) => {
          alert('Готово')
          console.log(response)
          this.getBooks()
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

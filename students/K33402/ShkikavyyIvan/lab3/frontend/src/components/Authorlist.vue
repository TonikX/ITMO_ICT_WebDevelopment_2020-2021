<template>
  <div>
    <div>
      <v-app-bar color="#653d19" dense dark>
        <v-btn icon @click="goHome">
          <v-icon>mdi-home</v-icon>
        </v-btn>
        <v-toolbar-title>Arthub</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn icon v-if="!isRedactor" @click="goLK">
          <v-icon>mdi-account</v-icon>
        </v-btn>
        <v-btn icon @click="logout">
          <v-icon>mdi-exit-to-app</v-icon>
        </v-btn>
      </v-app-bar>
    </div>
    <div class="block-content">
      <v-simple-table class="v-data-table">
        <template v-slot:default class="theme--light">
          <thead>
          <tr>
            <th class="text-center">
              <h2>Авторы</h2>
            </th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="author in authors" v-bind:key="author.id">
            <td>
              <router-link :to="{name:'Author', params:{id: author.id}}">{{ author.name }}</router-link>
              <v-btn v-if="isRedactor" color="error" icon @click="deleteAuthor(author.id)"><v-icon>mdi-delete</v-icon></v-btn>
            </td>
          </tr>
          </tbody>
          <v-btn v-if="isRedactor" color="primary" v-on:click="goNewAuthor">Добавить автора</v-btn>
        </template>
      </v-simple-table>
    </div>
  </div>
</template>

<script>
import $ from 'jquery'
export default {
  name: 'Authorlist',
  data () {
    return {
      authors: '',
      isRedactor: false
    }
  },
  created () {
    $.ajaxSetup({
      headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
    })
    this.loadRedactor()
    this.loadAuthors()
  },
  methods: {
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
    deleteAuthor (authorId) {
      $.ajax({
        url: 'http://127.0.0.1:8000/api/authors/' + authorId + '/delete/',
        type: 'DELETE',
        success: (response) => {
          alert('Запись удалена')
          this.loadAuthors()
        },
        error: (response) => {
          alert(response)
        }
      })
    },
    loadAuthors () {
      $.ajax({
        url: 'http://127.0.0.1:8000/api/authors/',
        type: 'GET',
        success: (response) => {
          this.authors = response
        },
        error: (response) => {
          alert(response)
        }
      })
    },
    goNewAuthor () {
      this.$router.push({ name: 'NewAuthor' })
    },
    goHome () {
      this.$router.push({ name: 'Home' })
    },
    goLK () {
      this.$router.push({ name: 'LK' })
    },
    logout () {
      sessionStorage.removeItem('auth_token')
      window.location = '/home'
    }
  }
}

</script>

<style scoped>
.block-content {
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: space-around;
  background: #fff0b5; /* Цвет фона */
  padding: 10px; /* Поля вокруг текста */
}
.v-data-table {
  line-height: 5;
  width: 700px;
  max-width: 100%;
}
.theme--light.v-data-table{
  background-color: #FFD7A7;
}
</style>

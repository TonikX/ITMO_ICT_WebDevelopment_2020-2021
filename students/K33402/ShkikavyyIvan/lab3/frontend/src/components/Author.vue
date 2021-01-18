<template>
  <div>
    <div>
      <v-app-bar color="#653d19" dense dark>
        <v-btn icon @click="goHome">
          <v-icon>mdi-home</v-icon>
        </v-btn>
        <v-toolbar-title>Arthub</v-toolbar-title>
        <v-btn class="ma-2" outlined color="white" @click="goAuthorlist">Лист авторов</v-btn>
        <v-spacer></v-spacer>
        <v-btn icon @click="goLK">
          <v-icon>mdi-account</v-icon>
        </v-btn>
        <v-btn icon @click="logout">
          <v-icon>mdi-exit-to-app</v-icon>
        </v-btn>
      </v-app-bar>
    </div>
    <div class="block-content">
      <div v-if="author">
        <v-card class="mx-auto" width="600" outlined>
          <v-list-item four-line>
            <v-list-item-content>
              <div class="overline mb-4">{{ author.name }}</div>
              <v-card-text class="pb-0">
                <p>{{ author.description }}</p>
              </v-card-text>
            </v-list-item-content>
          </v-list-item>
        </v-card>
      </div>
      <div>
        <h1>Произведения</h1>
        <v-card class="mx-auto" width="600" outlined>
          <v-simple-table class="v-data-table">
          <template v-slot:default class="theme--light">
            <thead>
            <tr>
              <th class="text-center">
                Название
              </th>
              <th class="text-center">
                Тип
              </th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="creation in creations" v-bind:key="creation.id">
              <td>
                <router-link :to="{name:'Creation', params:{id: creation.id}}">{{ creation.name }}</router-link>
              </td>
             <td>{{ creation.type }}</td>
            </tr>
            </tbody>
          </template>
        </v-simple-table>
        </v-card>
      </div>
    </div>
  </div>
</template>

<script>
import $ from 'jquery'
export default {
  name: 'Author',
  data () {
    return {
      author: '',
      creations: ''
    }
  },
  created () {
    $.ajaxSetup({
      headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
    })
    this.loadAuthor()
    this.loadCreation()
  },
  methods: {
    loadAuthor () {
      $.ajax({
        url: 'http://127.0.0.1:8000/api/authors/' + this.$route.params.id + '/',
        type: 'GET',
        success: (response) => {
          this.author = response
        },
        error: (response) => {
          alert(response)
        }
      })
    },
    loadCreation () {
      $.ajax({
        url: 'http://127.0.0.1:8000/api/authors/creation/' + this.$route.params.id + '/',
        type: 'GET',
        success: (response) => {
          this.creations = response
        },
        error: (response) => {
          alert(response)
        }
      })
    },
    goLK () {
      this.$router.push({ name: 'LK' })
    },
    goAuthorlist () {
      this.$router.push({ name: 'Authorlist' })
    },
    goHome () {
      this.$router.push({ name: 'Home' })
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
  justify-content: space-evenly;
  background: #fff0b5; /* Цвет фона */
  padding: 10px; /* Поля вокруг текста */
}
</style>

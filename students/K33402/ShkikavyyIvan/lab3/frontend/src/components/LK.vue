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
        <v-btn icon @click="logout">
          <v-icon>mdi-exit-to-app</v-icon>
        </v-btn>
      </v-app-bar>
    </div>
    <div class="block-content">
      <div v-if="user">
        <v-card class="mx-auto" max-width="450" outlined>
          <v-list-item four-line>
            <v-list-item-content>
              <div class="overline mb-4">{{ user.username }}</div>
              <v-list-item-title class="headline mb-7">
                {{ user.first_name }} {{ user.last_name }}
              </v-list-item-title>
              <v-list-item-subtitle>{{ user.email }}</v-list-item-subtitle>
              <v-card-actions class="button-card">
            <v-btn outlined rounded text color="primary" @click="loadEdit">Редактировать</v-btn>
          </v-card-actions>
            </v-list-item-content>
            <v-list-item-avatar tile size="80" color="green"></v-list-item-avatar>
          </v-list-item>
        </v-card>
      </div>
      <div v-if="!isRedactor">
        <h1>История отзывов</h1>
        <v-simple-table class="v-data-table">
          <template v-slot:default>
            <thead>
            <tr>
              <th class="text-center">
                Название
              </th>
              <th class="text-center">
                Оценка
              </th>
              <th class="text-center">
                Текст
              </th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="review in reviews" v-bind:key="review.id">
              <td>
                <router-link :to="{name:'Creation', params:{ id: review.creation.id }}">{{ review.creation.name }}
                </router-link>
              </td>
              <td>{{ review.rating }}</td>
              <td>{{ review.text }}</td>
              <td>
                <v-btn color="error" class="button" @click="deleteReview(review.id)">Удалить</v-btn>
                <v-btn color="primary" class="button"
                       @click="$router.push({ name: 'Review', params: { reviewId: review.id }})">
                  Редактировать
                </v-btn>
              </td>
            </tr>
            </tbody>
          </template>
        </v-simple-table>
      </div>
    </div>
  </div>
</template>

<script>
import $ from 'jquery'
export default {
  name: 'LK',
  data () {
    return {
      user: '',
      reviews: '',
      isRedactor: false
    }
  },
  created () {
    $.ajaxSetup({
      headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
    })
    this.loadInfo()
    this.loadReviews()
    this.loadRedactor()
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
    loadInfo () {
      $.ajax({
        url: 'http://127.0.0.1:8000/auth/users/me/',
        type: 'GET',
        success: (response) => {
          this.user = response
        },
        error: (response) => {
          alert(response)
        }
      })
    },
    loadEdit () {
      this.$router.push({ name: 'Editlc' })
    },
    loadReviews () {
      $.ajax({
        url: 'http://127.0.0.1:8000/api/reviews/',
        type: 'GET',
        success: (response) => {
          this.reviews = response
        },
        error: (response) => {
          alert(response)
        }
      })
    },
    deleteReview (reviewId) {
      $.ajax({
        url: 'http://127.0.0.1:8000/api/reviews/' + reviewId + '/delete/',
        type: 'DELETE',
        success: (response) => {
          alert('Запись удалена')
          this.loadReviews()
        },
        error: (response) => {
          alert(response)
        }
      })
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
  justify-content: space-around;
  background: #fff0b5; /* Цвет фона */
  padding: 10px; /* Поля вокруг текста */
}
.v-data-table {
  line-height: 2;
  width: 800px;
  max-width: 100%;
}
.button-card {
  margin: auto;
  text-align: center;
  display: block;
}
.button {
  margin: 8px;
}
</style>

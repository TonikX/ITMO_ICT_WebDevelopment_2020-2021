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
      <div v-if="creation">
        <v-card class="mx-auto" width="600" outlined>
          <v-list-item four-line>
            <v-list-item-content>
              <div class="overline mb-4">{{ creation.name }}</div>
              <v-list-item-title class="headline mb-7">
                <router-link :to="{name:'Author', params:{ id: creation.creator.id }}">{{creation.creator.name}}
                </router-link>
              </v-list-item-title>
              <v-card-text class="pb-0">
                <p>{{ creation.description }}</p>
              </v-card-text>
            </v-list-item-content>
          </v-list-item>
        </v-card>
      </div>
      <div>
        <h1>Отзывы</h1>
        <div class="comment-block" v-for="review in reviews" v-bind:key="review.id">
          <v-card class="mx-auto" max-width="400">
            <v-card-text class="headline font-weight-bold" data-md-color-primary="dark">
              {{ review.text }}
            </v-card-text>
            <v-card-actions>
              <v-list-item class="grow">
                <v-list-item-content>
                  <v-list-item-title>{{ review.author.username }}</v-list-item-title>
                </v-list-item-content>
                <v-row align="center" justify="end">
                  <v-icon class="mr-1">
                    mdi-heart
                  </v-icon>
                  <span class="subheading mr-2">{{ review.rating }}</span>
                </v-row>
              </v-list-item>
            </v-card-actions>
          </v-card>
          <!--<td>{{ review.author.username }}</td>
          <td>{{ review.text }}</td>
          <td>{{ review.rating }}</td>-->
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import $ from 'jquery'
export default {
  name: 'Creation',
  data () {
    return {
      creation: '',
      reviews: ''
    }
  },
  created () {
    $.ajaxSetup({
      headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
    })
    this.loadCreation()
    this.loadReviews()
  },
  methods: {
    loadCreation () {
      $.ajax({
        url: 'http://127.0.0.1:8000/api/creations/' + this.$route.params.id + '/',
        type: 'GET',
        success: (response) => {
          this.creation = response
        },
        error: (response) => {
          alert(response)
        }
      })
    },
    loadReviews () {
      $.ajax({
        url: 'http://127.0.0.1:8000/api/reviews/creation/' + this.$route.params.id + '/',
        type: 'GET',
        success: (response) => {
          this.reviews = response
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
.comment-block{
  margin: 10px;
}
</style>

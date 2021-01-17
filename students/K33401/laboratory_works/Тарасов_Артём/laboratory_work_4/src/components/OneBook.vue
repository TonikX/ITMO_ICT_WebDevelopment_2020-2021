<template>
  <div v-if="book">
    <div>
      <form>
        <v-text-field name="input" label="Id" v-model="id" type="text"></v-text-field>
        <v-text-field name="input" label="Owner" v-model="owner" type="text"></v-text-field>
        <v-text-field name="input" label="Author" v-model="author" type="text"></v-text-field>
        <v-text-field name="input" label="Name" v-model="name" type="text"></v-text-field>
        <v-text-field name="input" label="Section" v-model="section" type="text"></v-text-field>
        <v-text-field name="input" label="Pressmark" v-model="pressmark" type="text"></v-text-field>
        <v-btn class="select-line" color="#FFFF00" @click="putBook(book.id)">Обновить</v-btn>
      </form>
    </div>
  </div>
</template>

<script>
import $ from 'jquery'

export default {
  name: 'OneBook',
  created () {
    $.ajaxSetup({
      headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
    })
    this.getBook()
  },
  data () {
    return {
      id: '',
      owner: '',
      author: '',
      name: '',
      section: '',
      pressmark: '',
      book: ''
    }
  },
  methods: {
    getBook () {
      $.ajax({
        url: 'http://127.0.0.1:8005/api/books/' + this.$route.params.id + '/',
        type: 'GET',
        success: (response) => {
          console.log(response)
          this.book = response
          this.id = this.book.id
          this.owner = this.book.owner
          this.author = this.book.author
          this.name = this.book.name
          this.section = this.book.section
          this.pressmark = this.book.pressmark
        },
        error: (response) => {
          console.log(response)
        }
      })
    },
    putBook (id) {
      $.ajax({
        url: 'http://127.0.0.1:8005/api/books/' + id + '/',
        type: 'PUT',
        data: {
          id: this.id,
          owner: this.owner,
          author: this.author,
          name: this.name,
          section: this.section,
          pressmark: this.pressmark
        },
        success: (response) => {
          console.log(response)
        },
        error: (response) => {
          console.log(response)
        }
      })
    }
  }
}

</script>

<style scoped>

</style>

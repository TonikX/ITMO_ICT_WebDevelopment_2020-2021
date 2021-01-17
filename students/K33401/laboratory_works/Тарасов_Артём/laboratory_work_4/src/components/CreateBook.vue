<template>
  <div>
    <form>
      <v-text-field class="input" v-model="id" type="text" label="Id"></v-text-field>
      <v-text-field name="input" label="Owner" v-model="owner" type="text"></v-text-field>
      <v-text-field name="input" label="Author" v-model="author" type="text"></v-text-field>
      <v-text-field name="input" label="Name" v-model="name" type="text"></v-text-field>
      <v-text-field name="input" label="Section" v-model="section" type="text"></v-text-field>
      <v-text-field name="input" label="Pressmark" v-model="pressmark" type="text"></v-text-field>
      <v-btn class="select-line" color="#48ff3d" @click="postBook">Создать</v-btn>
    </form>
  </div>
</template>

<script>
import $ from 'jquery'

export default {
  name: 'CreateBook',
  created () {
    $.ajaxSetup({
      headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
    })
  },
  data () {
    return {
      id: '',
      owner: '',
      author: '',
      name: '',
      section: '',
      pressmark: ''
    }
  },
  methods: {
    postBook () {
      $.ajax({
        url: 'http://127.0.0.1:8005/api/books/',
        type: 'POST',
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

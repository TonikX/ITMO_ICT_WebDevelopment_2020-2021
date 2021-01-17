<template>
  <div>
    <div v-if="respObj">
      <form>
        <v-text-field name="input" label="Id" v-model="id" type="text"></v-text-field>
        <v-text-field name="input" label="Owner" v-model="owner" type="text"></v-text-field>
        <v-text-field name="input" label="Author" v-model="author" type="text"></v-text-field>
        <v-text-field name="input" label="Name" v-model="name" type="text"></v-text-field>
        <v-text-field name="input" label="Section" v-model="section" type="text"></v-text-field>
        <v-text-field name="input" label="Pressmark" v-model="pressmark" type="text"></v-text-field>
        <v-btn class="select-line" color="#FFFF00" @click="putObj(respObj.id)">Обновить</v-btn>
      </form>
    </div>
    <div v-if="!respObj">
      <form>
        <v-text-field name="input" label="Id" v-model="id" type="text"></v-text-field>
        <v-text-field name="input" label="Owner" v-model="owner" type="text"></v-text-field>
        <v-text-field name="input" label="Author" v-model="author" type="text"></v-text-field>
        <v-text-field name="input" label="Name" v-model="name" type="text"></v-text-field>
        <v-text-field name="input" label="Section" v-model="section" type="text"></v-text-field>
        <v-text-field name="input" label="Pressmark" v-model="pressmark" type="text"></v-text-field>
        <v-btn class="select-line" color="#48ff3d" @click="postObj">Создать</v-btn>
      </form>
    </div>
  </div>
</template>

<script>
import $ from 'jquery'

const baseUrlApi = 'http://127.0.0.1:8005/api/books/'
const backComp = 'Books'

export default {
  name: 'OneBook',
  created () {
    $.ajaxSetup({
      headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
    })
    if (this.$route.params.id) {
      this.getObj()
    }
  },
  data () {
    return {
      id: '',
      owner: '',
      author: '',
      name: '',
      section: '',
      pressmark: '',
      respObj: ''
    }
  },
  methods: {
    getObj () {
      $.ajax({
        url: baseUrlApi + this.$route.params.id + '/',
        type: 'GET',
        success: (response) => {
          console.log(response)
          this.respObj = response
          this.id = this.respObj.id
          this.owner = this.respObj.owner
          this.author = this.respObj.author
          this.name = this.respObj.name
          this.section = this.respObj.section
          this.pressmark = this.respObj.pressmark
        },
        error: (response) => {
          console.log(response)
        }
      })
    },
    putObj (id) {
      $.ajax({
        url: baseUrlApi + id + '/',
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
          this.$router.push({ name: backComp })
        },
        error: (response) => {
          alert(response)
          console.log(response)
        }
      })
    },
    postObj () {
      $.ajax({
        url: baseUrlApi,
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
          this.$router.push({ name: backComp })
          console.log(response)
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

</style>

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
      <v-card width="700" color="#fff8f2">
        <div class="label">Создание произведения</div>
        <form>
          <v-text-field class="input" v-model="name" type="text" label="Имя"></v-text-field>
          <v-container fluid>
            <v-textarea name="input-7-1" filled label="Описание произведения" auto-grow v-model="description"
                        type="text"></v-textarea>
          </v-container>
          <div class="sign-block">
            <v-col class="sign-block">
              <v-select class="select-line" v-model="type" :items="typeTips" label="Тип произведения" dense solo></v-select>
              <v-select class="select-line" v-model="creator" :items="authors" item-text="name" item-value="id" label="Автор" dense solo></v-select>
              <v-btn class="select-line" color="primary" @click="newCreation">Создать</v-btn>
            </v-col>
          </div>
        </form>
      </v-card>
    </div>
  </div>
</template>

<script>
import $ from 'jquery'

export default {
  name: 'NewCreation',
  data () {
    return {
      name: '',
      description: '',
      creator: '',
      type: '',
      authors: '',
      typeTips: ['Изобразительное искусство', 'Кино', 'Литература', 'Музыка']
    }
  },
  created () {
    $.ajaxSetup({
      headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
    })
    this.loadAuthors()
  },
  methods: {
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
    newCreation () {
      $.ajax({
        url: 'http://127.0.0.1:8000/api/creations/create/',
        type: 'POST',
        data: {
          name: this.name,
          description: this.description,
          creator: this.creator,
          type: this.type
        },
        success: (response) => {
          alert('Создано произведение')
          console.log(response)
          this.$router.push({ name: 'Home' })
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
.input{
  padding: 12px;
}
.label {
  margin-left: auto;
  margin-right: auto;
  margin-top: 10px;
  margin-bottom: 10px;
  text-decoration: none;
  font-family: 'Roboto', serif;
  font-style: normal;
  text-align: center;
  transition: .5s linear;
  width: 450px;
  font-size: 40px;
}
.sign-block {
  display: flex;
  justify-content: space-around;
  padding: 12px;
}
.select-line{
  margin: 2px;
}
</style>

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
      <v-card width="600" color="#fff8f2">
        <div class="label">Создание автора</div>
        <form>
          <v-text-field class="input" v-model="name" type="text" label="Имя"></v-text-field>
          <v-container fluid>
            <v-textarea name="input-7-1" filled label="Описание автора" auto-grow v-model="description" type="text"></v-textarea>
          </v-container>
          <div class="sign-block">
            <v-btn color="primary" @click="newAuthor">Сохранить</v-btn>
          </div>
        </form>
      </v-card>
    </div>
  </div>
</template>

<script>
import $ from 'jquery'
export default {
  name: 'NewAuthor',
  data () {
    return {
      name: '',
      description: ''
    }
  },
  created () {
    $.ajaxSetup({
      headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
    })
  },
  methods: {
    newAuthor () {
      $.ajax({
        url: 'http://127.0.0.1:8000/api/authors/create/',
        type: 'POST',
        data: {
          name: this.name,
          description: this.description
        },
        success: (response) => {
          alert('Создан автор')
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
  text-align: left;
  padding: 12px;
}
</style>

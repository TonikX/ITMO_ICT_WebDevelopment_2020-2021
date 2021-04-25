<template>
  <div>
    <router-link :to="{name:'Books'}">Книги</router-link>
    <br/>
    <router-link :to="{name:'Readers'}">Читатели</router-link>
    <br/>
    <router-link :to="{name:'InstancesOfBook'}">Экземпляр книги</router-link>
    <br/>
    <router-link :to="{name:'Issu ingAInstances'}">Данные о выдаче</router-link>
    <br/>
    <form>
      <v-text-field name="input" label="Id" v-model="id" type="text"></v-text-field>
      <v-text-field name="input" label="first_name" v-model="first_name" type="text"></v-text-field>
      <v-text-field name="input" label="last_name" v-model="last_name" type="text"></v-text-field>
      <v-text-field name="input" label="username" v-model="username" type="text"></v-text-field>
      <v-btn class="select-line" color="#FFFF00" @click="updateUser">Обновить</v-btn>
    </form>
  </div>
</template>

<script>

import $ from 'jquery'

export default {
  name: 'ChooseInterface',

  data () {
    return {
      first_name: '',
      last_name: '',
      id: '',
      username: ''
    }
  },
  created () {
    $.ajaxSetup({
      headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
    })
    this.getUser()
  },
  methods: {
    /**
     * Function for update user
     */
    updateUser () {
      $.ajax({
        url: 'http://127.0.0.1:8005/auth/users/me/',
        type: 'PUT',
        data: {
          first_name: this.first_name,
          last_name: this.last_name
        },
        success: (response) => {
          console.log('Успешно')
        },
        error: (response) => {
          alert(response.responseText + '\n' + response.statusText)
        }
      })
    },
    getUser () {
      $.ajax({
        url: 'http://127.0.0.1:8005/auth/users/me/',
        type: 'GET',
        success: (response) => {
          console.log(response)
          this.respObj = response
          this.first_name = this.respObj.first_name
          this.last_name = this.respObj.last_name
          this.id = this.respObj.id
          this.username = this.respObj.username
        },
        error: (response) => {
          alert(response.responseText + '\n' + response.statusText)
        }
      })
    }
  }
}
</script>

<style scoped>

</style>

<template>
  <div>
    <div v-if="respObj">
      <form>
        <v-text-field name="input" label="Id" v-model="id" type="text"></v-text-field>
        <v-text-field name="input" label="Owner" v-model="owner" type="text"></v-text-field>
        <v-text-field name="input" label="Full Name" v-model="full_name" type="text"></v-text-field>
        <v-text-field name="input" label="Passport Number" v-model="passport_number" type="text"></v-text-field>
        <v-text-field name="input" label="Birthday" v-model="birthday" type="text"></v-text-field>
        <v-text-field name="input" label="Address" v-model="address" type="text"></v-text-field>
        <v-text-field name="input" label="Phone" v-model="phone" type="text"></v-text-field>
        <v-text-field name="input" label="Degree" v-model="degree" type="text"></v-text-field>
        <v-text-field name="input" label="Graduate degree"  v-model="graduate_degree" type="text"></v-text-field>
        <v-btn class="select-line" color="#FFFF00" @click="putObj(respObj.id)">Обновить</v-btn>
      </form>
    </div>
    <div v-if="!respObj">
        <form>
          <v-text-field name="input" label="Id" v-model="id" type="text"></v-text-field>
          <v-text-field name="input" label="Owner" v-model="owner" type="text"></v-text-field>
          <v-text-field name="input" label="Full Name" v-model="full_name" type="text"></v-text-field>
          <v-text-field name="input" label="Passport Number" v-model="passport_number" type="text"></v-text-field>
          <v-text-field name="input" label="Birthday" v-model="birthday" type="text"></v-text-field>
          <v-text-field name="input" label="Address" v-model="address" type="text"></v-text-field>
          <v-text-field name="input" label="Phone" v-model="phone" type="text"></v-text-field>
          <v-text-field name="input" label="Degree" v-model="degree" type="text"></v-text-field>
          <v-text-field name="input" label="Graduate degree"  v-model="graduate_degree" type="text"></v-text-field>
          <v-btn class="select-line" color="#48ff3d" @click="postObj">Создать</v-btn>
        </form>
    </div>
  </div>
</template>

<script>
import $ from 'jquery'

const baseUrlApi = 'http://127.0.0.1:8005/api/readers/'
const backComp = 'Readers'

export default {
  name: 'OneReader',
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
      full_name: '',
      passport_number: '',
      birthday: '',
      address: '',
      phone: '',
      degree: '',
      graduate_degree: '',
      respObj: ''
    }
  },
  methods: {
    /**
     * Function for getting data object
     */
    getObj () {
      $.ajax({
        url: baseUrlApi + this.$route.params.id + '/',
        type: 'GET',
        success: (response) => {
          console.log(response)
          this.respObj = response
          this.id = this.respObj.id
          this.owner = this.respObj.owner
          this.full_name = this.respObj.full_name
          this.passport_number = this.respObj.passport_number
          this.birthday = this.respObj.birthday
          this.address = this.respObj.address
          this.phone = this.respObj.phone
          this.degree = this.respObj.degree
          this.graduate_degree = this.respObj.graduate_degree
        },
        error: (response) => {
          alert(response.responseText + '\n' + response.statusText)
        }
      })
    },
    /**
     * Function for change data object
     * @param {number} id
     */
    putObj (id) {
      $.ajax({
        url: baseUrlApi + id + '/',
        type: 'PUT',

        data: {
          id: this.id,
          owner: this.owner,
          full_name: this.full_name,
          passport_number: this.passport_number,
          birthday: this.birthday,
          address: this.address,
          phone: this.phone,
          degree: this.degree,
          graduate_degree: this.graduate_degree
        },
        success: (response) => {
          console.log(response)
          this.$router.push({ name: backComp })
        },
        error: (response) => {
          alert(response.responseText + '\n' + response.statusText)
          console.log(response)
        }
      })
    },
    /**
     * Function for create data object
     */
    postObj () {
      $.ajax({
        url: baseUrlApi,
        type: 'POST',

        data: {
          id: this.id,
          owner: this.owner,
          full_name: this.full_name,
          passport_number: this.passport_number,
          birthday: this.birthday,
          address: this.address,
          phone: this.phone,
          degree: this.degree,
          graduate_degree: this.graduate_degree
        },
        success: (response) => {
          this.$router.push({ name: backComp })
          console.log(response)
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

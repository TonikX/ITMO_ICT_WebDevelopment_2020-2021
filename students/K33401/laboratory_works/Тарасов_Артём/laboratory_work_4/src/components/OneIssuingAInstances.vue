<template>
  <div>
    <div v-if="respObj">
      <form>
        <v-text-field name="input" label="Owner" v-model="owner" type="text"></v-text-field>
        <v-text-field name="input" label="return_date" v-model="return_date" type="text"></v-text-field>
        <v-text-field name="input" label="id_instance" v-model="instance" type="text"></v-text-field>
        <v-text-field name="input" label="id_reader" v-model="reader" type="text"></v-text-field>
        <v-btn class="select-line" color="#FFFF00" @click="putObj(respObj.id)">Обновить</v-btn>
      </form>
    </div>
    <div v-if="!respObj">
      <form>
        <v-text-field name="input" label="Owner" v-model="owner" type="text"></v-text-field>
        <v-text-field name="input" label="return_date" v-model="return_date" type="text"></v-text-field>
        <v-text-field name="input" label="id_instance" v-model="instance" type="text"></v-text-field>
        <v-text-field name="input" label="id_reader" v-model="reader" type="text"></v-text-field>
        <v-btn class="select-line" color="#48ff3d" @click="postObj">Создать</v-btn>
      </form>
    </div>
  </div>
</template>

<script>
import $ from 'jquery'

const baseUrlApi = 'http://127.0.0.1:8005/api/issuingAInstances/'
const backComp = 'IssuingAInstances'

export default {
  name: 'OneIssuingAInstances',
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
      return_date: '',
      start_date: '',
      instance: '',
      reader: '',
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
          this.return_date = this.respObj.return_date
          this.instance = this.respObj.instance
          this.start_date = this.respObj.start_date
          this.reader = this.respObj.reader
        },
        error: (response) => {
          alert(response.responseText + '\n' + response.statusText)
          console.log(response)
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
          start_date: this.start_date,
          return_date: this.return_date,
          instance: this.instance,
          reader: this.reader
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
          start_date: this.start_date,
          return_date: this.return_date,
          instance: this.instance,
          reader: this.reader
        },
        success: (response) => {
          this.$router.push({ name: backComp })
          console.log(response)
        },
        error: (response) => {
          alert(response.responseText + '\n' + response.statusText)
          console.log(response)
        }
      })
    }
  }
}

</script>

<style scoped>

</style>

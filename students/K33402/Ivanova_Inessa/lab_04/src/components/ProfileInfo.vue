<template>
  <div>
  <div>
    <input id="tel" v-model="tel" class="window" type="number" />
  </div>
  <div>
    <input id="height" v-model="height" class="window" type="number"/>
  </div>
  <div>
    <input id="weight" v-model="weight" class="window" type="number"/>
  </div>
    <button type="button" @click="saveChanges">Сохранить</button>
  </div>
</template>

<script>
import $ from 'jquery'

export default {
  name: 'ProfileInfo',
  methods: {
    saveChanges () {
      $.ajax({
        url: 'http://127.0.0.1:8000/auth/users/me/',
        type: 'PUT',
        data: {
          tel: this.tel,
          height: this.height,
          weight: this.weight
        },
        success: (response) => {
          alert('Данные изменены')
          location.reload()
        }
      })
    }
  },
  props: {
    tel: Number,
    height: Number,
    weight: Number
  },
  data: () => ({
    tel: '',
    height: '',
    weight: ''
  }),
  created () {
  }
}
</script>

<style>
</style>

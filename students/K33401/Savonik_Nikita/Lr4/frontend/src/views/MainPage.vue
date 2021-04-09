<template>
 <v-main>
   <header-component :logged-in="loggedIn"/>
   <v-row class="my-2" >
     <v-col cols="6" class="mx-auto" id="block">
       <epic-item-card
         v-for="cat in cats"
         :key="cat.id"
         :cat="cat"
         class="my-2"
       />
     </v-col>
   </v-row>
</v-main>
</template>

<script>
import HeaderComponent from '../components/Header'
import EpicItemCard from '../components/EpicItemCard'

export default {
  name: 'MainPage',
  components: { EpicItemCard, HeaderComponent },
  data: () => ({
    cats: [],
    loggedIn: false
  }),
  created () {
    this.loggedIn = !!localStorage.getItem('token')
    this.getCats()
  },
  methods: {
    /**
     * Отправляет Get запрос на получение всех кошек из базы
     * @returns {Promise<void>}
     */
    async getCats () {
      const response = await this.axios.get('http://127.0.0.1:8000/api/cats/')
      this.cats = response.data.reverse()
    }
  }
}
</script>

<style scoped>
  #block {
    min-width: 1000px;
  }
</style>

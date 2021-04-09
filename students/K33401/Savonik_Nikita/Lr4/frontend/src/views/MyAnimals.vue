<template>
 <v-main>
   <header-component :logged-in="loggedIn"/>
   <v-row class="my-2" >
     <modal-add-cat />
     <v-col cols="12" class="mx-auto" id="block">
       <v-card min-width="400px" max-width="400px" class="mx-auto my-12">

          <v-list>
            <v-list-item-group
            v-model="selectedItem"
            color="primary"
            >
            <v-list-item class="my-3" v-for="cat in cats" :key="cat.id">
              <v-list-item-title>{{cat.name}}</v-list-item-title>
              <v-btn color="#005B7C" elevation="0" dark v-on:click="delCat(cat.id)">Удалить</v-btn>
            </v-list-item>
              </v-list-item-group>
          </v-list>
       </v-card>
     </v-col>
   </v-row>
</v-main>
</template>

<script>
import ModalAddCat from '../components/ModalAddCat'
import HeaderComponent from '../components/Header'
export default {
  name: 'MyAnimals',
  components: { HeaderComponent, ModalAddCat },
  data: () => ({
    cats: [],
    loggedIn: false
  }),
  created () {
    this.loggedIn = !!localStorage.getItem('token')
    if (!this.loggedIn) {
      this.$router.push('/')
    }
    this.getCats()
  },
  methods: {
    /**
     * Удаляет кошку из базы данных
     * @param id
     * @returns {Promise<void>}
     */
    async delCat (id) {
      await this.axios.delete(`http://127.0.0.1:8000/api/cats/${id}/delete/`, { headers: { Authorization: `Token ${localStorage.getItem('token')}` } })
      this.getCats()
    },
    /**
     * Получение кошек владельца из базы данных
     * @returns {Promise<void>}
     */
    async getCats () {
      const response = await this.axios.get('http://127.0.0.1:8000/api/ownercats/', { headers: { Authorization: `Token ${localStorage.getItem('token')}` } })
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

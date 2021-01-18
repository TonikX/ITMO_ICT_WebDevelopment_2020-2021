<template>
  <section>
    <Header />
    <NavBar />
    <table class="programms" cellpadding="30">
      <tr v-for="classItem in classes"
          :key="classItem.identifier">
        <th>{{ classItem.name }}</th>
        <td>{{ classItem.description }}</td>
      </tr>
    </table>
    <Footer />
  </section>
</template>

<script>
import Header from '@/components/Header'
import NavBar from '@/components/NavBar'
import Footer from '@/components/Footer'

export default {
  name: 'Classes',

  metaInfo: {
    title: 'Групповые программы',
    meta: [{
      name: 'viewport',
      content: 'width=device-width, initial-scale=1'
    }]
  },
  components: {
    Header,
    NavBar,
    Footer
  },
  data: () => ({
    classes: []
  }),
  methods: {
    /**
     * Функция получает список типов уроков с описаниями в переменную this.classes
     */
    async getClasses () {
      try {
        const response = await this.axios
          .get('http://127.0.0.1:8000/lessons/')
        if (response.status !== 200) {
          throw new Error(response.error)
        }
        this.classes = response.data
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    }
  },

  created () {
    this.getClasses()
  }
}
</script>

<style>
  .programms {
    width: 80%;
    margin: 20px auto 20px auto;
    text-align: left;
    border-left: 2px solid red;
  }
</style>

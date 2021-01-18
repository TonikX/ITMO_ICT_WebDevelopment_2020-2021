<template>
  <section>
    <Header />
    <NavBar />
    <div class="gallery-container">
      <h1>Наши тренеры</h1>
      <div class="row">
        <figure class="photo"
                v-for="coach in coaches"
                :key="coach.identifier">
          <img class="center" src="./../assets/c1.jpg" alt="coach">
          <figcaption>
            <h4>{{ coach.name }}</h4>
            {{ coach.description }}
          </figcaption>
        </figure>
      </div>
    </div>
    <Footer />
  </section>
</template>

<script>
import Header from '@/components/Header'
import NavBar from '@/components/NavBar'
import Footer from '@/components/Footer'

export default {
  name: 'Coaches',

  metaInfo: {
    title: 'Тренеры',
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
    coaches: []
  }),
  methods: {
    /**
     * Функция получает список всех тренеров в переменную this.coaches
     */
    async getCoaches () {
      try {
        const response = await this.axios
          .get('http://127.0.0.1:8000/coaches/')
        if (response.status !== 200) {
          throw new Error(response.error)
        }
        this.coaches = response.data
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    }
  },

  created () {
    this.getCoaches()
  }
}
</script>

<style>
.gallery-container {
  width: 90%;
  margin: 10px auto 0;
}
.photo {
  float: left;
  width: 33.333333%;
  padding: 10px;
  box-sizing: border-box;
}
.photo img {
  max-width: 100%;
  display: block;
  height: auto;
  margin-right: auto;
  margin-left: auto;
}
figcaption {
  text-align: center;
}
h1 {
  text-align: center;
}
</style>

<template>
    <section>

      <greeting-card :username="savedUsername" />

      <h2>Проект на Vue.</h2>

      <v-form @submit.prevent="submitUsername"
              ref="form"
              class="my-2"
      >
        <v-row>
          <v-col cols="3" class="mx-auto">
            <v-text-field
              label="Ведите своё имя"
              v-model="username"
              name="username"
              placeholder="Иван Иванович"
            />
          </v-col>
        </v-row>
      </v-form>
      <br>
      <h3>Варианты приветсвий:</h3>

      <v-row>
        <v-col cols="4" class="mx-auto">
          <v-card
           elevation="2"
           class="px-2 py-5"
           color="primary"
           dark
          >
            <greeting-list :greetings="greetings" />
          </v-card>
        </v-col>
      </v-row>
    </section>
</template>

<script>
import GreetingCard from '../components/GreetingCard'
import GreetingList from '../components/GreetingList'

export default {
  name: 'Greeting',
  components: {
    GreetingList,
    GreetingCard
  },
  data: () => ({
    username: '',
    savedUsername: '',
    greetings: [
      { id: 1, text: 'Привет' },
      { id: 2, text: 'Hello' },
      { id: 3, text: 'Hola' }
    ]
  }),

  methods: {
    submitUsername () {
      localStorage.setItem('username', this.username)
      this.savedUsername = this.username
      this.username = ''
      console.log(this.savedUsername)
      this.$refs.form.reset()
    }

  },
  created () {
    if (localStorage.getItem('username')) {
      this.savedUsername = localStorage.getItem('username')
      console.log('kek')
    }
  }
}

</script>

<style scoped>
.greeting-list-wrapper {
  display: flex;
}
</style>

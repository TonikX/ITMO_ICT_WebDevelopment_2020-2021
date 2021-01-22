<template>
  <section>
    <toolbar :is-logged="isLogged"
             @IsLoggedChanged="setIsLogged"/>

    <v-row class="d-flex align-center text-center my-1 mx-2" fluid>
      <v-col cols="6" class="mx-auto">
        <h1 >Создание опроса</h1>
      </v-col>
    </v-row>

    <v-row class="d-flex align-center text-center my-1 mx-2" fluid>
      <v-col cols="6" class="mx-auto">
        <v-text-field
          v-model="title"
          label="Название"
          required
        />
      </v-col>
    </v-row>
    <v-row class="d-flex align-center text-center my-1 mx-2" fluid>
      <v-col cols="6" class="mx-auto">
        <v-text-field
          v-model="theme"
          label="Тема"
          required
        />
      </v-col>
    </v-row>
    <v-row class="d-flex align-center text-center my-1 mx-2" fluid>
      <v-col cols="6" class="mx-auto">
        <v-text-field
          v-model="description"
          label="Описание"
          required
          aria-multiline="true"
        />
      </v-col>
    </v-row>
    <v-row class="d-flex align-center text-center my-1 mx-2" fluid>
      <v-col cols="6" class="mx-auto">
        <v-text-field
          v-model="voting_time"
          label="Время прохождения"
          type="number"
          required
        />
      </v-col>
    </v-row>
    <v-row class="d-flex align-center text-center my-1 mx-2" fluid v-for="(question, index) in question_set"
           :key="question.id">
      <v-col cols="6" class="mx-auto">
        <question
          :index="index"
          :answer_set="question.answer_set"
          :question="question"
          @Description="addDescription"
          @RemoveQuestion="removeQuestion"/>
      </v-col>
    </v-row>
    <v-btn v-if="!poll" dark large color="primary" fixed right bottom @click="createPoll">
      Создать
    </v-btn>
    <v-btn v-else dark large color="primary" fixed right bottom @click="createPoll">
      Изменить
    </v-btn>
    <v-row class="d-flex align-center text-center my-1 mx-2" fluid>
      <v-col cols="6" class="mx-auto">
        <v-btn dark large color="primary" @click="addQuestion">
          Добавить вопрос
        </v-btn>
      </v-col>
    </v-row>
  </section>
</template>

<script>
import Toolbar from '../components/main/Toolbar'
import { BASE_URL, TOKEN_KEY } from '../variables'
import router from '../router'
import SignIn from './auth/SignIn'
import Question from '../components/create/Question'

export default {
  name: 'Create',
  components: { Question, Toolbar },
  props: {
    poll: Object
  },
  data: () => ({
    isLogged: Boolean,
    title: '',
    description: '',
    theme: '',
    voting_time: 0,
    question_set: []
  }),
  methods: {
    /**
     * Выставляет флаг, залогинен ли пользователь
     * @param data
     */
    setIsLogged (data) {
      this.isLogged = data
      if (!data) {
        router.push({ name: 'Home', params: { isHome: true } }).catch(() => {})
      }
    },
    /**
     * Добавляет вопрос
     */
    addQuestion () {
      this.question_set.push({
        answer_set: [
          {
            description: ''
          },
          {
            description: ''
          }
        ],
        description: ''
      })
      console.log(this.question_set)
    },
    /**
     * Удаляет вопрос
     * @param index
     */
    removeQuestion (index) {
      this.question_set.splice(index, 1)
    },
    /**
     * Создает опрос
     */
    async createPoll () {
      const config = {
        headers:
          {
            Authorization: `Token ${sessionStorage.getItem(TOKEN_KEY)}`
          }
      }
      const body = {
        title: this.title,
        description: this.description,
        theme: this.theme,
        voting_time: this.voting_time,
        question_set: this.question_set
      }
      const success = (response) => {
        console.log(response)
        router.push({ name: 'Details', params: { pollId: response.data.id } })
      }

      const fail = (error) => {
        console.log(error)
      }
      if (this.poll) {
        this.axios.put(`${BASE_URL}/polls/${this.poll.id}/update/`, body, config)
          .then((response) => {
            success(response)
          }, (error) => {
            fail(error)
          })
      } else {
        this.axios.post(`${BASE_URL}/polls/create/`, body, config)
          .then((response) => {
            success(response)
          }, (error) => {
            fail(error)
          })
      }
    },
    /**
     * Добавляет описание вопроса
     * @param data
     */
    addDescription (data) {
      console.log(data)
      this.question_set[data.index].description = data.description
    }
  },

  created () {
    this.isLogged = sessionStorage.getItem(TOKEN_KEY) !== null
    if (this.isLogged) {
      if (this.poll) {
        this.title = this.poll.title
        this.description = this.poll.description
        this.theme = this.poll.theme
        this.voting_time = this.poll.voting_time
        this.question_set = this.poll.question_set
      } else {
        this.addQuestion()
      }
    } else {
      router.push(SignIn)
    }
  }

}
</script>

<style scoped>

</style>

<template>
  <section>
    <toolbar :is-logged="isLogged"/>
    <v-container fluid class="d-flex flex-column text-center my-12 " >
      <v-container fluid class="d-flex justify-end" style="padding-right: 20%" v-if="poll.is_my">
          <v-btn @click="updatePoll">Изменить</v-btn>
          <v-btn @click="deletePoll" class="mx-3">Удалить</v-btn>
      </v-container>
    <v-row>
      <v-col style="margin-top: 16px; margin-right: auto; margin-left: auto;">
        <h2>{{poll.title}}</h2>
      </v-col>
    </v-row>

      <v-row>
        <v-col cols="6" style="margin: auto">
        <question
          v-for="question in poll.question_set"
          style="margin: 16px"
          :key="question.id"
          :question="question"
          :is-my="poll.is_my"
          :poll-id="poll.id"
          @CustomEventInputChanged="addAnswer"
        />
      </v-col>
    </v-row>
    <v-row>
      <v-col class="mx-auto">
        <v-btn
          class="mr-4"
          @click="submit"
          v-if="!poll.is_voted"
        >
          Проголосовать
        </v-btn>
        <v-card-text v-else>Вы уже проголосовали</v-card-text>
      </v-col>
    </v-row>

    </v-container>
  </section>

</template>

<script>
import { BASE_URL, TOKEN_KEY } from '../variables'
import Question from '../components/detail/Question'
import Toolbar from '../components/main/Toolbar'
import router from '../router'

export default {
  name: 'Details',
  components: { Question, Toolbar },

  data: function () {
    return {
      poll: Object,
      answerList: [],
      isLogged: Boolean,
    }
  },

  methods: {
    /**
     * Отправляет запрос на получени деталей опроса
     */
    async getPollDetail () {
      try {
        const token = sessionStorage.getItem(TOKEN_KEY)
        let config = {}
        if (token) {
          config = {
            headers:
              {
                Authorization: `Token ${token}`
              }
          }
        }
        const response = await this.axios
          .get(`${BASE_URL}/polls/${this.$route.params.pollId}`, config)

        if (response.status !== 200) {
          throw new Error(response.error)
        }

        console.log(response.data)

        this.poll = response.data
        this.$forceUpdate()
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    /**
     * По отдельности сохраняет ответы пользователя
     */
    async submit () {
      console.log(this.answerList)
      for (const el of this.answerList) {
        await this.sendAnswer(el.answer_id)
        await this.getPollDetail()
        console.log(el.answer_id)
      }
    },
    /**
     * Отправляет запрос на голосование в опросе
     * @param answerId
     */
    async sendAnswer (answerId) {
      const token = sessionStorage.getItem(TOKEN_KEY)
      let config = {}
      if (token) {
        config = {
          headers:
            {
              Authorization: `Token ${token}`
            }
        }
      }
      this.axios.post(`${BASE_URL}/user_to_answer/create/`, {
        answer: answerId
      }, config)
        .then((response) => {
          console.log(response)
        }, (error) => {
          console.log(error)
        })
    },
    /**
     * Добавляет вопрос
     * @param data
     */
    addAnswer (data) {
      const existedAnswer = this.answerList.find(el => el.question_id === data.question.id)
      if (existedAnswer) {
        existedAnswer.answer_id = data.id
      } else {
        this.answerList.push({
          question_id: data.question,
          answer_id: data.id
        })
      }
      console.log(this.answerList)
    },
    /**
     * Удаляет голосование
     */
    deletePoll () {
      const token = sessionStorage.getItem(TOKEN_KEY)
      let config = {}
      if (token) {
        config = {
          headers:
            {
              Authorization: `Token ${token}`
            }
        }
      }
      this.axios.delete(`${BASE_URL}/polls/${this.poll.id}/delete/`, config)
        .then(() => {
          router.push({ name: 'Home', params: { isHome: true } }).catch(() => {})
        }, (error) => {
          console.log(error)
        })
    },
    /**
     * Переход на страницу обновления голосования
     */
    updatePoll () {
      router.push({ name: 'Create', params: { poll: this.poll } })
    }
  },

  created () {
    this.getPollDetail()
    this.isLogged = sessionStorage.getItem(TOKEN_KEY) !== null
  }
}
</script>

<style scoped>

</style>

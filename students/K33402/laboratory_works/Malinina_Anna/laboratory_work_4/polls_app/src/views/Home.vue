<template>
    <section>
        <toolbar :is-logged="isLogged"
                 @IsLoggedChanged="setIsLogged"/>
        <v-row class="d-flex align-center text-center my-6" fluid>
            <v-col cols="9" class="mx-auto">
                <h1>Опросы</h1>
            </v-col>
        </v-row>
        <v-row v-if="isLogged" class="d-flex justify-start" fluid>
            <v-col cols="4" class="mx-auto">
                <v-select
                        :items="items"
                        label="Фильтр"
                        solo
                        v-model="defaultSelected"
                        @change="loadPolls"
                ></v-select>
            </v-col>
        </v-row>
        <v-row class="d-flex align-center text-center" fluid>
            <v-col cols="9" class="mx-auto">
                <poll
                        v-for="poll in polls"
                        style="margin: 8px"
                        :key="poll.id"
                        :poll="poll"
                />
            </v-col>
        </v-row>
        <v-btn v-if="isLogged" fab dark large color="primary" fixed right bottom @click="addPoll">
            <v-icon color="white" large>mdi-plus</v-icon>
        </v-btn>
    </section>

</template>

<script>
import Poll from '../components/main/Poll'
import { BASE_URL, TOKEN_KEY } from '../variables'
import Toolbar from '../components/main/Toolbar'
import router from '../router'
import Create from './Create'

export default {
  name: 'Home',
  components: { Poll, Toolbar },
  props: {
    isHome: Boolean
  },

  data: () => ({
    polls: [],
    isLogged: Boolean,
    showMyPolls: false,
    items: ['Все опросы', 'Мои опросы'],
    defaultSelected: 'Все опросы'
  }),

  methods: {
      /**
       * Получение списка опросов
       */
    async getPolls () {
      try {
        let url = ''
        if (this.showMyPolls) {
          url = `${BASE_URL}/polls?current=1`
        } else {
          url = `${BASE_URL}/polls/`
        }
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
          .get(url, config)

        if (response.status !== 200) {
          throw new Error(response.error)
        }

        this.polls = response.data.map((poll) => {
          const date = new Date(poll.create_date)

          const year = date.getFullYear()

          const month = String(date.getMonth() + 1).length > 1
            ? date.getMonth() + 1
            : `0${date.getMonth() + 1}`

          const day = String(date.getDate()).length > 1
            ? date.getDate()
            : `0${date.getDate()}`

          poll.create_date = `${year}/${month}/${day}`
          console.log(poll)
          return poll
        })
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
      /**
       * Переход на страницу создания опроса
       */
    addPoll () {
      router.push(Create)
    },
      /**
       * Смена флага, залогинен ли пользователь
       * @param data
       */
    setIsLogged (data) {
      this.isLogged = data
    },
      /**
       * Загружает опросы
       */
    loadPolls () {
      this.showMyPolls = this.defaultSelected === 'Мои опросы'
      this.getPolls()
    }
  },

  created () {
    if (this.isHome) {
      this.showMyPolls = !this.isHome
    }
    this.getPolls()
    this.isLogged = sessionStorage.getItem(TOKEN_KEY) !== null
  }
}
</script>

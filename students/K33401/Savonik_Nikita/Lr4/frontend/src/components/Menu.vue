<template>
    <v-menu class="my-0 py-0"
      :close-on-content-click="false"
      :nudge-width="250"
      offset-y
    >
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          color="black"
          dark
          v-bind="attrs"
          v-on="on"
        >
          Мой профиль
        </v-btn>
      </template>

      <v-card>
        <v-list>
          <v-list-item>

            <v-list-item-content>
              <v-list-item-title> <h3>{{ username }}</h3></v-list-item-title>
            </v-list-item-content>

            <v-list-item-action>
              <v-btn
                icon
                v-on:click="logout"
              >
                <v-icon v-html="icon"></v-icon>
              </v-btn>
            </v-list-item-action>
          </v-list-item>
        </v-list>

        <v-divider></v-divider>
        <v-row>
         <v-col cols="12" class="mx-auto" id="card">
           <v-card class="text-center" elevation="0">
             <v-card-subtitle class="text-left">Информация о пользователе</v-card-subtitle>
             <v-card-text class="text-left" id="text"><b>Никнейм: </b>{{ info.username }} <br>
               <b>Имя: </b>{{ info.first_name }} <br>
               <b>Фамилия: </b>{{ info.last_name }} <br>
               <b>Адрес: </b>{{ info.address }} </v-card-text>
           </v-card>
           <v-card class="my-5 mx-0" flat>
             <modal-edit-window :info="info" />
           </v-card>
      </v-col>
       </v-row>
      </v-card>
    </v-menu>
</template>

<script>
import {
  mdiLocationExit
} from '@mdi/js'

import ModalEditWindow from '../components/ModalEditWindow'
const host = 'http://127.0.0.1:8000/api/'
export default {
  name: 'MenuComponent',
  components: { ModalEditWindow },
  data: () => ({
    username: localStorage.getItem('username'),
    icon: mdiLocationExit,
    token: null,
    info: Object,
    loggedIn: false
  }),
  methods: {
    /**
     * Выход из системы
     */
    logout () {
      this.$router.push('/signout')
    },
    /**
     * Получение информации о пользователе из базы дынных
     * @returns {Promise<void>}
     */
    async getInfo () {
      const response = await this.axios.get(host + 'auth/users/me/', { headers: { Authorization: `Token ${this.token}` } })
      this.info = response.data
    }
  },
  created () {
    this.token = localStorage.getItem('token')
    this.loggedIn = !!this.token
    if (!this.loggedIn) {
      this.$router.push('/')
    }
    this.getInfo()
  }
}
</script>

<style scoped>
  #text {
    font-size: 18px;
    line-height: 28px;
  }
  #card {
    min-width: 400px;
    max-width: 400px;

  }

  #block {
    margin-top: 200px;
  }

  main{
    background-color: #EFEFEE;
  }
  #cat {
    float: right;
    margin-top: -24px;
  }

</style>

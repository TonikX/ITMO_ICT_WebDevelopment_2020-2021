<template>
  <section>
    <toolbar :is-logged="isLogged"
             @IsLoggedChanged="setIsLogged"/>
    <v-alert
      dismissible
      v-model="error"
      type="error"
    >{{errorText}}</v-alert>
    <v-row class="d-flex align-center my-6" fluid>
      <v-col cols="9" class="mx-auto">
        <h1>Профиль</h1>
    <v-tabs vertical class="my-3 mx-12" style="width: 90%; margin: auto">
      <v-tab>
        Мои данные
      </v-tab>
      <v-tab>
        Изменить данные
      </v-tab>
      <v-tab>
        Изменить пароль
      </v-tab>

      <v-tab-item>
        <v-card flat>
          <v-card-text>
            Имя: {{ this.firstName}}<br>
            Фамилия: {{this.lastName}}<br>
            Никнейм: {{this.username}}<br>
            Email: {{this.email}}
          </v-card-text>
        </v-card>
      </v-tab-item>

      <v-tab-item>
        <v-card flat>
          <form>

            <v-text-field
              v-model="firstName"
              label="Имя"
              required
            ></v-text-field>

            <v-text-field
              v-model="lastName"
              label="Фамилия"
              required
            ></v-text-field>

            <v-text-field
              v-model="email"
              label="E-mail"
              required
            ></v-text-field>

            <v-btn
              class="mr-4"
              @click="saveProfileInfo"
            >
              Сохранить
            </v-btn>
          </form>
        </v-card>
      </v-tab-item>

      <v-tab-item>
        <v-card flat>
          <form>
            <v-text-field
              v-model="oldPassword"
              label="Текущий пароль"
              required
            ></v-text-field>
            <v-text-field
              v-model="password"
              label="Новый пароль"
              required
            ></v-text-field>

            <v-text-field
              v-model="password2"
              label="Повторите пароль"
              required
            ></v-text-field>

            <v-btn
              class="mr-4"
              @click="savePassword"
              :disabled="password !== password2 || password === '' || oldPassword === ''"
            >
              Сохранить
            </v-btn>
          </form>
        </v-card>
      </v-tab-item>

    </v-tabs>
      </v-col>
    </v-row>
  </section>
</template>

<script>
import { BASE_URL, TOKEN_KEY } from '../variables'
import router from '../router'
import SignIn from './auth/SignIn'
import Toolbar from '../components/main/Toolbar'

export default {
  name: 'Profile',
  components: { Toolbar },
  data: () => ({
    user: Object,
    config: {},
    firstName: '',
    lastName: '',
    username: '',
    email: '',
    password: '',
    password2: '',
    oldPassword: '',
    error: false,
    errorText: ''
  }),
  methods: {
    /**
     * Смена флага, залогинен ли пользователь
     * @param data
     */
    setIsLogged (data) {
      this.isLogged = data
      if (!data) {
        router.push({ name: 'Home', params: { isHome: true } }).catch(() => {})
      }
    },
    /**
     * Получение текущего пользователя
     */
    getCurrentUser () {
      this.axios.get(`${BASE_URL}/auth/users/me/`, this.config)
        .then((response) => {
          this.user = response.data
          this.firstName = this.user.first_name
          this.lastName = this.user.last_name
          this.username = this.user.username
          this.email = this.user.email
        }, (error) => {
          console.log(error)
        })
    },
    /**
     * Сохранение пользовательской информации
     */
    saveProfileInfo () {
      this.axios.put(`${BASE_URL}/auth/users/me/`, {
        first_name: this.firstName,
        last_name: this.lastName,
        email: this.email,
        date_of_birth: this.date
      }, this.config)
    },
    /**
     * Сохранение нового пароля
     */
    savePassword () {
      this.axios.post(`${BASE_URL}/auth/users/set_password/`, {
        new_password: this.password,
        current_password: this.oldPassword
      }, this.config)
        .then((response) => {
          this.user = response.data
          this.firstName = this.user.first_name
          this.lastName = this.user.last_name
          this.username = this.user.username
          this.email = this.user.email
        }, (error) => {
          console.log(error)
          this.errorText = 'Не удалось поменять пароль'
          this.error = true
        })
    }
  },
  created () {
    const token = sessionStorage.getItem(TOKEN_KEY)
    this.isLogged = token !== null
    this.config = {
      headers:
        {
          Authorization: `Token ${token}`
        }
    }
    if (this.isLogged) {
      this.getCurrentUser()
    } else {
      router.push(SignIn)
    }
  }
}
</script>

<style scoped>

</style>

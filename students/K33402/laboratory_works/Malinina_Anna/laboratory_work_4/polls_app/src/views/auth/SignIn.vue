<template>
  <section>
    <toolbar :is-logged="false"/>
    <v-row class="d-flex align-center text-center my-12" fluid>
      <v-col cols="4" class="mx-auto">
        <v-card
          elevation="2"
          class="px-2 py-5"
          color="primary"
          dark
        >
          <form>
            <v-text-field
              v-model="username"
              :error-messages="UsernameErrors"
              label="Никнейм"
              required
              @input="this.$v.name.$touch()"
              @blur="this.$v.name.$touch()"
            ></v-text-field>

            <v-text-field
              v-model="password"
              :error-messages="PasswordErrors"
              label="Пароль"
              :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
              :type="show1 ? 'text' : 'password'"
              required
              @input="this.$v.name.$touch()"
              @blur="this.$v.name.$touch()"
              @click:append="show1 = !show1"
            ></v-text-field>

            <v-btn
              class="mr-4"
              @click="submit"
            >
              Войти
            </v-btn>
          </form>
          <v-card-text>
            <router-link style="cursor: pointer; color: deepskyblue" :to="{ name: 'SignUp'}">Зарегистрироваться</router-link>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </section>

</template>

<script>
import { validationMixin } from 'vuelidate'
import { required } from 'vuelidate/lib/validators'
import { BASE_URL, TOKEN_KEY } from '../../variables'
import router from '../../router'
import Toolbar from '../../components/main/Toolbar'
import SignUp from './SignUp'

export default {
  name: 'SignIn',
  components: { Toolbar },
  mixins: [validationMixin],

  validations: {
    username: { required },
    password: { required }
  },

  data: () => ({
    valid: true,
    username: '',
    password: '',
    show1: false
  }),

  computed: {
    /**
     * Добавляет ошибку никнейма и возвращает массив ошибок
     * @return Array
     */
    UsernameErrors () {
      const errors = []
      if (!this.$v.username.$dirty) return errors
      !this.$v.username.required && errors.push('Поле обязательно')
      return errors
    },
    /**
     * Добавляет ошибку пароля и возвращает массив ошибок
     * @return Array
     */
    PasswordErrors () {
      const errors = []
      if (!this.$v.password.$dirty) return errors
      !this.$v.password.required && errors.push('Поле обязательно')
      return errors
    }
  },

  methods: {
    /**
     * Отправляет запрос на авторизацию
     */
    submit () {
      this.$v.$touch()
      if (!this.$v.$invalid) {
        this.axios.post(`${BASE_URL}/auth/token/login`, {
          username: this.username,
          password: this.password
        })
          .then((response) => {
            sessionStorage.setItem(TOKEN_KEY, response.data.auth_token)
            this.$parent.isLogged = true
            router.push({ name: 'Home', params: { isHome: true } }).catch(() => {})
          }, (error) => {
            console.log(error)
          })
      }
    }
  }
}
</script>

<style scoped>

</style>

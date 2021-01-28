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
              @input="this.$v.text.$touch()"
              @blur="this.$v.text.$touch()"
            ></v-text-field>

            <v-text-field
              v-model="firstName"
              :error-messages="FirstNameErrors"
              label="Имя"
              required
              @input="this.$v.text.$touch()"
              @blur="this.$v.text.$touch()"
            ></v-text-field>

            <v-text-field
              v-model="lastName"
              :error-messages="LastNameErrors"
              label="Фамилия"
              required
              @input="this.$v.text.$touch()"
              @blur="this.$v.text.$touch()"
            ></v-text-field>

            <v-text-field
              v-model="email"
              :error-messages="emailErrors"
              label="E-mail"
              required
              @input="this.$v.email.$touch()"
              @blur="this.$v.email.$touch()"
            ></v-text-field>

            <v-text-field
              v-model="password"
              :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
              :type="show1 ? 'text' : 'password'"
              :error-messages="PasswordErrors"
              required
              hint="Пароль"
              @input="this.$v.email.$touch()"
              @blur="this.$v.email.$touch()"
              @click:append="show1 = !show1"
            ></v-text-field>

            <v-btn
              class="mr-4"
              @click="submit"
            >
              Зарегистрироваться
            </v-btn>
          </form>
        </v-card>
      </v-col>
    </v-row>
  </section>

</template>

<script>
import { validationMixin } from 'vuelidate'
import { required, email } from 'vuelidate/lib/validators'
import router from '../../router'
import { BASE_URL, TOKEN_KEY } from '../../variables'
import Toolbar from '../../components/main/Toolbar'

export default {
  name: 'SignIn',

  mixins: [validationMixin],

  components: { Toolbar },

  validations: {
    firstName: { required },
    lastName: { required },
    username: { required },
    email: { required, email },
    password: { required }
  },

  data: () => ({
    valid: true,
    firstName: '',
    lastName: '',
    username: '',
    email: '',
    password: '',
    show1: false
  }),

  watch: {
    menu (val) {
      val && setTimeout(() => (this.$refs.picker.activePicker = 'YEAR'))
    }
  },

  computed: {
    /**
     * Добавляет ошибку имени и возвращает массив ошибок
     * @return Array
     */
    FirstNameErrors () {
      const errors = []
      if (!this.$v.firstName.$dirty) return errors
      !this.$v.firstName.required && errors.push('Поле обязательно')
      return errors
    },
    /**
     * Добавляет ошибку фамилии и возвращает массив ошибок
     * @return Array
     */
    LastNameErrors () {
      const errors = []
      if (!this.$v.lastName.$dirty) return errors
      !this.$v.lastName.required && errors.push('Поле обязательно')
      return errors
    },
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
    },
    /**
     * Добавляет ошибку почты и возвращает массив ошибок
     * @return Array
     */
    emailErrors () {
      const errors = []
      if (!this.$v.email.$dirty) return errors
      !this.$v.email.email && errors.push('Некорректный электронный адрес')
      !this.$v.email.required && errors.push('E-mail обязателен')
      return errors
    }
  },

  methods: {
    /**
     * Отправляет запрос на регистрацию
     */
    submit () {
      this.$v.$touch()
      if (!this.$v.$invalid) {
        this.axios.post(`${BASE_URL}/auth/users/`, {
          first_name: this.firstName,
          last_name: this.lastName,
          username: this.username,
          password: this.password,
          email: this.email
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

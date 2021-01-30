<template>
  <div class="signup">
    <v-form
      @submit.prevent="signUp"
      ref="signUpForm"
      class="my-2"
    >
      <v-row>
        <v-col cols="3" class="mx-auto">
          <v-text-field
            label="Введите имя"
            v-model="signUpForm.first_name"
          />
          <v-text-field
            label="Введите фамилию"
            v-model="signUpForm.last_name"
          />
          <v-text-field
            label="Введите паспорт"
            v-model="signUpForm.passport"
          />
          <v-text-field
            label="Введите электронную почту"
            v-model="signUpForm.email"
          />
          <v-text-field
            label="Введите имя пользователя"
            v-model="signUpForm.username"
          />
          <v-text-field
            label="Введите пароль"
            v-model="signUpForm.password"
            type="password"
          />
          <v-btn type="submit" color="black" dark>Зарегистрироваться</v-btn>

          <p class="mt-5">Уже зарегистрированы? <router-link to="/signin">Войти</router-link></p>
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>

<script>
export default {
  name: 'SignUp',

  data: () => ({
    signUpForm: {
      first_name: '',
      last_name: '',
      passport: '',
      email: '',
      username: '',
      password: ''
    }
  }),

  methods: {
    async signUp () {
      try {
        const response = await this.axios
          .post('http://127.0.0.1:8000/auth/users/', this.signUpForm)

        if (response.status !== 201) {
          throw new Error(response.status)
        }

        this.$refs.signUpForm.reset()
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    }
  }
}
</script>

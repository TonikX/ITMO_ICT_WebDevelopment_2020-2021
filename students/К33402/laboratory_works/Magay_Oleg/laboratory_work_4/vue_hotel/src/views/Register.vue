<template>
  <div class="register">
    <v-form
      @submit.prevent="register"
      ref="signUpForm"
      class="my-2"
    >
      <v-row>
        <v-col cols="3" class="mx-auto">
          <v-text-field
            label="Введите email"
            v-model="regForm.email"
          />
          <v-text-field
            label="Введите логин"
            v-model="regForm.username"
          />
          <v-text-field
            label="Введите пароль"
            v-model="regForm.password"
            type="password"
          />
          <v-btn color="primary" @click="register">Register</v-btn>
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>

<script>
export default {
  name: 'Register',
  data: () => ({
    regForm: {
      email: '',
      username: '',
      password: ''
    }
  }),
  methods: {
    async register () {
      await this.axios
        .post('http://127.0.0.1:8000/auth/users/', this.regForm)
        .then((res) => {
          console.log(res)
          window.location.href = 'http://localhost:8080/login'
        })
        .catch((error) => {
          console.log(error)
          alert('Введены некорректные данные! Проверьте правильность ввода.')
        })
    }
  }
}
</script>

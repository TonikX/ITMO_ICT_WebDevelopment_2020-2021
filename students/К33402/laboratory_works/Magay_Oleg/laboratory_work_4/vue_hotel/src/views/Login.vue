<template>
  <div class="login">
    <v-form
      @submit.prevent="login"
      ref="loginForm"
      class="my-2"
    >
      <v-row>
        <v-col cols="3" class="mx-auto">
          <v-text-field
            label="Введите логин"
            v-model="loginForm.username"
          />
          <v-text-field
            label="Введите пароль"
            v-model="loginForm.password"
            type="password"
          />
          <v-btn color="primary" @click='login'>Войти</v-btn>
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>

<script>
export default {
  name: 'Login',
  data: () => ({
    loginForm: {
      username: '',
      password: ''
    }
  }),
  methods: {
    async login () {
      const token = await this.axios
        .post('http://127.0.0.1:8000/auth/token/login/', this.loginForm)
        .then((res) => {
          console.log(res)
          return res.data.auth_token
        })
        .catch((error) => {
          console.log(error)
          alert('Неверный логин или пароль!')
        })
      localStorage.setItem('token', token)
      window.location.href = 'http://localhost:8080/'
    }
  }
}
</script>

<template>
  <div>
    <v-form
      @submit.prevent="enter"
      ref="login"
      class="my-2"
    >
      <v-row>
        <v-col cols="3" class="mx-auto">
          <v-text-field
            label="Введите логин:"
            v-model="login.username"
          />
          <v-text-field
            label="Введите пароль:"
            v-model="login.password"
            type="password"
          />
          <v-btn @click='enter'>Войти</v-btn>

          <p class="mt-5"><router-link to="/createuser">Зарегистрироваться</router-link></p>
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>

<script>

export default {
  name: 'Login',
  data: () => ({
    login: {
      username: '',
      password: ''
    }
  }),
  methods: {
    enter: async function () {
      await this.axios
        .post('http://127.0.0.1:8000/auth/token/login/', this.login)
        .then((res) => {
          localStorage.setItem('auth_token', res.data.auth_token)
          console.log(`Token ${localStorage.getItem('auth_token')}`)
          window.location.href = '/'
        })
        .catch((error) => {
          console.log(error)
          if (error.request.status === 400) {
            alert('Логин или пароль не верен')
          }
        })
    }
  }
}
</script>
<style scoped>
</style>

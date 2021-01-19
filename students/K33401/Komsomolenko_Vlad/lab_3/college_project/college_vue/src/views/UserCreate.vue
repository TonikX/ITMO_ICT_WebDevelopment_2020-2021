<template>
  <div>
    <v-form
      @submit.prevent="CreateUser"
      ref="userCr"
      class="my-2"
    >
      <v-row>
        <v-col cols="3" class="mx-auto">
          <v-text-field
            label="Введите email:"
            v-model="userCr.email"
          />
          <v-text-field
            label="Введите логин:"
            v-model="userCr.username"
          />
          <v-text-field
            label="Введите пароль:"
            v-model="userCr.password"
            type="password"
          />
          <v-btn @click='CreateUser'>Зарегистрироваться</v-btn>

          <p class="mt-5"><router-link to="/login">Войти</router-link></p>
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>

<script>
export default {
  name: 'UserCreate',
  data: () => ({
    userCr: {
      email: '',
      username: '',
      password: ''
    }
  }),
  methods: {
    async CreateUser () {
      await this.axios
        .post('http://127.0.0.1:8000/auth/users/', this.userCr)
        .then((res) => {
          console.log(res)
          window.location.href = '/login'
        })
        .catch((error) => {
          console.log(error)
          if (error.request.status === 400) {
            alert('Усп! Произошла ошибка, возможно вы неправильно указали данные =(')
          }
        })
    }
  }
}
</script>

<style scoped>

</style>

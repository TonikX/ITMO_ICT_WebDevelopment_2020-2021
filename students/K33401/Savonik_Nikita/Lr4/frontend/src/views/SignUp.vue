<template>
    <v-main>
    <header-component />
    <v-row id="auth-form">
      <v-col cols="4" class="mx-auto" id="auth-block">
        <v-card>
        <v-card-title  id="color_">Регистрация</v-card-title>
        <v-card-text id="space">
          <v-form class="my-0" id="space2" v-if="!error" @submit="signUp" ref="form">
            <v-text-field label="Никнейм" v-model="username"></v-text-field>
            <v-text-field label="Имя" v-model="firstName"></v-text-field>
            <v-text-field label="Фамилия" v-model="lastName"></v-text-field>
            <v-text-field label="Адрес" v-model="address"></v-text-field>
            <v-text-field label="Пароль" v-model="password" type="password"></v-text-field>
            <v-btn type="submit" dark color="#008EAB" class="mx-0 my-4" id="enter" width="200px">Зарегистрироваться</v-btn>
          </v-form>
          <v-form class="my-0" id="space2" v-else @submit="signUp" ref="form">
            <p id="error">Пользователь не может быть создан</p>
            <v-text-field label="Никнейм" v-model="username"></v-text-field>
            <v-text-field label="Имя" v-model="firstName"></v-text-field>
            <v-text-field label="Фамилия" v-model="lastName"></v-text-field>
            <v-text-field label="Адрес" v-model="address"></v-text-field>
            <v-text-field label="Пароль" v-model="password" type="password"></v-text-field>
            <v-btn type="submit" dark color="#008EAB" class="mx-0 my-4" id="enter" width="200px">Зарегистрироваться</v-btn>
          </v-form>
        </v-card-text>
    </v-card>
      </v-col>
    </v-row>

  </v-main>
</template>

<script>
import HeaderComponent from '../components/Header'
const host = 'http://127.0.0.1:8000/api/'

export default {
  name: 'SignUp',
  components: { HeaderComponent },
  created () {
    if (localStorage.getItem('token')) {
      this.$router.push('/')
    }
  },
  data: () => ({
    username: null,
    password: null,
    address: null,
    firstName: null,
    lastName: null,
    error: null
  }),
  methods: {
    /**
     * Регестрирует пользователя
     * @param event
     */
    signUp (event) {
      event.preventDefault()
      this.axios.post(host + 'auth/users/',
        {
          username: this.username,
          password: this.password,
          address: this.address,
          first_name: this.firstName,
          last_name: this.lastName
        })
        .then(response => {
          if (response.status === 201) {
            this.$router.push('/signin')
          } else {
            this.$refs.form.reset()
            this.error = true
          }
        })
        .catch(_ => {
          this.error = true
          this.$refs.form.reset()
        })
      this.$refs.form.reset()
    }
  }
}
</script>

<style scoped>
  #auth-form{
    margin-top: 5%;

  }

  #auth-block {
    min-width: 400px;
    max-width: 800px;
  }

  .primary{
    color: white;
  }

  #space {
    padding-bottom: 0px;
  }

  #space2 {
    padding-top: 20px;
  }

  #enter {
    height: 40px;
  }

  #color_ {
    background-color: #005B7C;
    color: white;
  }

    #error {
    font-size: 17px;
    text-align: center;
    padding-top: 8px;
    background-color: darkred;
    height: 40px;
    color: white;
  }
  main{
    background-color: #EFEFEE;
  }

</style>

<template>
  <div class="block-content">
    <v-card width="600" color="#fff8f2">
      <h1>Регистрация</h1>
      <validation-observer ref="observer" v-slot="{ invalid }">
        <validation-provider v-slot="{ errors }" name="Никнейм" rules="required|max:10">
          <v-text-field v-model="username" class="input" :counter="10" :error-messages="errors" label="Никнейм" required></v-text-field>
        </validation-provider>
        <validation-provider v-slot="{ errors }" name="Поле" rules="required">
          <v-text-field v-model="password" class="input" type="password" :error-messages="errors" label="Пароль" required></v-text-field>
        </validation-provider>
        <validation-provider v-slot="{ errors }" name="Поле" rules="required">
          <v-text-field v-model="password2" class="input" type="password" :error-messages="errors" label="Повторите пароль" required></v-text-field>
        </validation-provider>
        <validation-provider v-slot="{ errors }" name="Поле" rules="required|email">
          <v-text-field v-model="email" class="input" :error-messages="errors" label="E-mail" required></v-text-field>
        </validation-provider>
        <validation-provider v-slot="{ errors }" name="Имя" rules="required">
          <v-text-field v-model="first_name" class="input" :error-messages="errors" label="Имя" required></v-text-field>
        </validation-provider>
        <validation-provider v-slot="{ errors }" name="Фамилия" rules="required">
          <v-text-field v-model="last_name" class="input" :error-messages="errors" label="Фамилия" required></v-text-field>
        </validation-provider>
        <v-btn class="button" type="submit" :disabled="invalid" @click="passwordCheck">Регистрация</v-btn>
    </validation-observer>
    </v-card>
  </div>
</template>

<script>
import { required, digits, email, max } from 'vee-validate/dist/rules'
import { extend, ValidationObserver, ValidationProvider, setInteractionMode } from 'vee-validate'
import $ from 'jquery'
setInteractionMode('eager')
extend('digits', {
  ...digits,
  message: '{_field_} needs to be {length} digits. ({_value_})'
})
extend('required', {
  ...required,
  message: '{_field_} не должно быть пустым'
})
extend('max', {
  ...max,
  message: '{_field_} may not be greater than {length} characters'
})
extend('email', {
  ...email,
  message: 'Заполните верно почту'
})
export default {
  components: {
    ValidationProvider,
    ValidationObserver
  },
  name: 'Signin',
  data () {
    return {
      username: '',
      password: '',
      password2: '',
      email: '',
      first_name: '',
      last_name: ''
    }
  },
  methods: {
    passwordCheck () {
      if (this.password === this.password2) {
        this.signUp()
      } else {
        alert('Пароли не совпадают')
      }
    },
    signUp () {
      $.ajax({
        url: 'http://127.0.0.1:8000/auth/users/',
        type: 'POST',
        data: {
          username: this.username,
          password: this.password,
          email: this.email,
          first_name: this.first_name,
          last_name: this.last_name
        },
        success: (response) => {
          alert('Регистрация прошла успешно')
          sessionStorage.setItem('auth_token', response.auth_token)
          this.$router.push({ name: 'Login' })
        },
        error: (response) => {
          if (response.status === 400) {
            alert('Некорректное имя пользователя и/или пароль')
          }
        }
      })
    }
  }
}
</script>

<style scoped>
.block-content {
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: space-around;
  background: #fff0b5; /* Цвет фона */
  padding: 10px; /* Поля вокруг текста */
}
.button{
  width:150px;
  margin: 10px;
}
.input{
  width:300px;
  margin: auto;
}
</style>

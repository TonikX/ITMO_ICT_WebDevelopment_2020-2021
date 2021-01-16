<template>
  <div>
    <div>
      <v-app-bar color="#653d19" dense dark>
        <v-btn icon @click="goHome">
          <v-icon>mdi-home</v-icon>
        </v-btn>
        <v-toolbar-title>Arthub</v-toolbar-title>
        <v-btn class="ma-2" outlined color="white" @click="goAuthorlist">Лист авторов</v-btn>
        <v-spacer></v-spacer>
        <v-btn icon @click="goLK">
          <v-icon>mdi-account</v-icon>
        </v-btn>
        <v-btn icon @click="logout">
          <v-icon>mdi-exit-to-app</v-icon>
        </v-btn>
      </v-app-bar>
    </div>
    <div class="block-content">
      <v-card width="600" color="#fff8f2">
        <h1>Изменение пароля</h1>
        <validation-observer ref="observer" v-slot="{ invalid }">
            <validation-provider v-slot="{ errors }" name="Поле" rules="required">
              <v-text-field v-model="current_password" class="input" type="password" :error-messages="errors"
                            label="Предыдущий пароль" required></v-text-field>
            </validation-provider>
            <validation-provider v-slot="{ errors }" name="Поле" rules="required">
              <v-text-field v-model="password" class="input" type="password" :error-messages="errors"
                            label="Новый пароль" required></v-text-field>
            </validation-provider>
            <validation-provider v-slot="{ errors }" name="Поле" rules="required">
              <v-text-field v-model="password2" class="input" type="password" :error-messages="errors"
                            label="Повторите пароль" required></v-text-field>
            </validation-provider>
            <v-btn class="button" type="submit" color="primary" :disabled="invalid" @click="passwordCheck">Сохранить
            </v-btn>
        </validation-observer>
      </v-card>
      <v-card width="600" color="#fff8f2">
        <h1>Редактирование</h1>
        <validation-observer ref="observer" v-slot="{ invalid }">
            <validation-provider v-slot="{ errors }" name="Поле" rules="required|email">
              <v-text-field v-model="email" class="input" :error-messages="errors" label="E-mail"
                            required></v-text-field>
            </validation-provider>
            <validation-provider v-slot="{ errors }" name="Имя" rules="required">
              <v-text-field v-model="first_name" class="input" :error-messages="errors" label="Имя"
                            required></v-text-field>
            </validation-provider>
            <validation-provider v-slot="{ errors }" name="Фамилия" rules="required">
              <v-text-field v-model="last_name" class="input" :error-messages="errors" label="Фамилия"
                            required></v-text-field>
            </validation-provider>
            <v-btn class="button" type="submit" color="primary" :disabled="invalid" @click="correctInfo">Сохранить
            </v-btn>
        </validation-observer>
      </v-card>
    </div>
  </div>
</template>

<script>
import $ from 'jquery'
import { required, digits, email, max } from 'vee-validate/dist/rules'
import { extend, ValidationObserver, ValidationProvider, setInteractionMode } from 'vee-validate'
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
  name: 'Editlc',
  data () {
    return {
      current_password: '',
      password: '',
      password2: '',
      email: '',
      first_name: '',
      last_name: ''
    }
  },
  created () {
    $.ajaxSetup({
      headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
    })
    this.loadInfo()
  },
  methods: {
    passwordCheck () {
      if (this.password === this.password2) {
        this.correctPassword()
      } else {
        alert('Пароли не совпадают')
      }
    },
    correctPassword () {
      $.ajax({
        url: 'http://127.0.0.1:8000/auth/users/set_password/',
        type: 'POST',
        data: {
          new_password: this.password,
          current_password: this.current_password
        },
        success: (response) => {
          console.log(response)
          this.$router.push({ name: 'LK' })
        }
      })
    },
    correctInfo () {
      $.ajax({
        url: 'http://127.0.0.1:8000/auth/users/me/',
        type: 'PATCH',
        data: {
          email: this.email,
          first_name: this.first_name,
          last_name: this.last_name
        },
        success: (response) => {
          console.log(response)
          this.$router.push({ name: 'LK' })
        },
        error: (response) => {
          alert(response)
        }
      })
    },
    loadInfo () {
      $.ajax({
        url: 'http://127.0.0.1:8000/auth/users/me/',
        type: 'GET',
        success: (response) => {
          this.email = response.email
          this.first_name = response.first_name
          this.last_name = response.last_name
        },
        error: (response) => {
          alert(response)
        }
      })
    },
    goAuthorlist () {
      this.$router.push({ name: 'Authorlist' })
    },
    goHome () {
      this.$router.push({ name: 'Home' })
    },
    goLK () {
      this.$router.push({ name: 'LK' })
    },
    logout () {
      sessionStorage.removeItem('auth_token')
      window.location = '/home'
    }
  }
}
</script>

<style scoped>
.block-content {
  margin: auto;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: space-around;
  background: #fff0b5; /* Цвет фона */
  padding: 10px; /* Поля вокруг текста */
}
</style>

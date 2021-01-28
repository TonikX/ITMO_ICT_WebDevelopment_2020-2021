# Интерфейсы

## Регистрация

#### - /auth/users/ (POST)

- username
- password1
- password2
- email
- first_name
- last_name

# Запросы к серверу

#### Регистрация пользователей

```js
export default {
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
```
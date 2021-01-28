# Интерфейсы

## Авторизация

#### - /auth/token/login/ (POST)

- username
- password

# Запросы к серверу

#### Аутентификация пользователей

```js
export default {
    name: 'Login',
    data() {
        return {
            login: '',
            password: ''
        }
    },
    methods: {
        setLogin() {
            $.ajax({
                url: 'http://127.0.0.1:8000/auth/token/login/',
                type: 'POST',
                data: {
                    username: this.login,
                    password: this.password
                },
                success: (response) => {
                    sessionStorage.setItem('auth_token', response.auth_token)
                    this.$router.push({name: 'Home'})
                },
                error: (response) => {
                    if (response.status === 400) {
                        alert('Логин или пароль не верен')
                    }
                }
            })
        }
    }
}  
```

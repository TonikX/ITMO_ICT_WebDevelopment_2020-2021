# Интерфейсы

## Изменение данных пользователя

#### - /auth/users/me/ (PATCH)

- email
- first_name
- last_name

#### - /auth/users/set_password/ (POST)

- current_password
- password 
- password2

# Запросы к серверу

#### Изменение данных пользователей

```js
export default {
    name: 'Editlc',
    data() {
        return {
            current_password: '',
            password: '',
            password2: '',
            email: '',
            first_name: '',
            last_name: ''
        }
    },
    created() {
        $.ajaxSetup({
            headers: {Authorization: 'Token ' + sessionStorage.getItem('auth_token')}
        })
        this.loadInfo()
    },
    methods: {
        passwordCheck() {
            if (this.password === this.password2) {
                this.correctPassword()
            } else {
                alert('Пароли не совпадают')
            }
        },
        correctPassword() {
            $.ajax({
                url: 'http://127.0.0.1:8000/auth/users/set_password/',
                type: 'POST',
                data: {
                    new_password: this.password,
                    current_password: this.current_password
                },
                success: (response) => {
                    console.log(response)
                    this.$router.push({name: 'LK'})
                }
            })
        },
        correctInfo() {
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
                    this.$router.push({name: 'LK'})
                },
                error: (response) => {
                    alert(response)
                }
            })
        },
        loadInfo() {
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
        }
    }
}
```
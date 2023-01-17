# Login

Авторизация пользователя

**URL** : `/login`

**Methods** : `POST`

## Success Responses

**Code** : `201 Created`

**Content** : `{}`

```javascript
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
```
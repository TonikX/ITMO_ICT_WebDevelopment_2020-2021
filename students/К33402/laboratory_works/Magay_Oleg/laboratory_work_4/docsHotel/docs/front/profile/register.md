# Register

Регистрация пользователя

**URL** : `/register`

**Methods** : `POST`

## Success Responses

**Code** : `201 Created`

**Content** : `{}`

```javascript
    async register () {
      await this.axios
        .post('http://127.0.0.1:8000/auth/users/', this.regForm)
        .then((res) => {
          console.log(res)
          window.location.href = 'http://localhost:8080/login'
        })
        .catch((error) => {
          console.log(error)
          alert('Введены некорректные данные! Проверьте правильность ввода.')
        })
    }
}
```
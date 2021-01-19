# Login

Вход

**URL** : `/login`

**Methods** : `POST`

## Success Responses

**Code** : `201 Created`

**Content** : `{}`

```javascript
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
```
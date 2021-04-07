##User authentication

###Sign In

Аутентифицировать пользователя, создать токен и перенаправить на страницу, соответсвующую типу пользователя

**URL** : `/auth/token/login/`

**Methods** : `POST`

#### Success Responses

**Code** : `201 Created`

**Content** : `{}`

```javascript
    async signIn () {
      const token = await this.axios
        .post('http://127.0.0.1:8000/auth/token/login/', this.signInForm)
        .then((res) => {
          console.log(res)
          return res.data.auth_token
        })
        .catch((error) => {
          console.log(error)
          alert('Invalid username or password!')
        })
      localStorage.setItem('token', token)
      this.axios.defaults.headers.common.Authorization = `Token ${localStorage.getItem('token')}`
      const userType = await this.axios
        .get('http://127.0.0.1:8000/auth/users/me/')
        .then((res) => {
          console.log(res.data)
          return res.data
        })
      if (userType.type === 'manager') {
        window.location.href = 'http://localhost:8080/manager'
      } else if (userType.type === 'deputy') {
        window.location.href = 'http://localhost:8080/deputy'
      }
    }
}
```}

# User Sign Up 

Зарегистрировать нового пользователя

**URL** : `/auth/users/`

**Methods** : `POST`

## Success Responses

**Code** : `201 Created`

**Content** : `{}`

```javascript
    async signUp () {
      await this.axios
        .post('http://127.0.0.1:8000/auth/users/', this.signUpForm)
        .then((res) => {
          console.log(res)
          window.location.href = 'http://localhost:8080/signin'
        })
        .catch((error) => {
          console.log(error)
        })
    }
}
```

### Sign Up 

Зарегистрировать нового пользователя

**URL** : `/auth/users/`

**Methods** : `POST`

#### Success Responses

**Code** : `201 Created`

**Content** : `{}`

```javascript
    async signUp () {
      await this.axios
        .post('http://127.0.0.1:8000/auth/users/', this.signUpForm)
        .then((res) => {
          console.log(res)
          window.location.href = 'http://localhost:8080/signin'
        })
        .catch((error) => {
          console.log(error)
        })
    }
}
```
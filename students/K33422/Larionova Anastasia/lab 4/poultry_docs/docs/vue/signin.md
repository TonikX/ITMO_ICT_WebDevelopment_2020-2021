# Authorization

Аутентифицирует нового пользователя в системе

**URL** : `/auth/token/login/`

**Methods** : `POST`

## Success Responses

**Code** : `200 OK`

**Content** : `{}`

```javascript
async signIn () {
      try {
        const response = await this.axios
          .post('http://127.0.0.1:8000/auth/token/login/', this.signInForm)

        console.log('SIGN IN RESPONSE', response)

        this.$refs.signInForm.reset()

        localStorage.setItem('token', response.data.auth_token)

        this.$router.push('/settings')
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    }
```
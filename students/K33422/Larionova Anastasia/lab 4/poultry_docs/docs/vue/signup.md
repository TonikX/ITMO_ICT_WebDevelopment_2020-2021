# New user's creation

Аутентифицирует нового пользователя в системе

**URL** : `/auth/users/`

**Methods** : `POST`

## Success Responses

**Code** : `201 Created`

**Content** : `{}`

```javascript
async signUp () {
      try {
        const response = await this.axios
          .post('http://127.0.0.1:8000/auth/users/', this.signUpForm)

        if (response.status !== 201) {
          throw new Error(response.status)
        }

        this.$refs.signUpForm.reset()
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    }
```
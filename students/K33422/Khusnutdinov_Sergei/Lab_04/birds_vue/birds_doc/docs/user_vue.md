# Sign in / Sign Up

Allows to log in or create a new user

**URL** : `/auth/token/login/`

**Methods** : `POST`

Success Responses

**Code** : `200 OK`

**Content** : `{}`

```javascript
<script>
export default {
  name: 'SignIn',
  data: () => ({
    signInForm: {
      password: '',
      username: ''
    }
  }),
  methods: {
    async signIn () {
      try {
        const response = await this.axios
          .post('http://127.0.0.1:8000/auth/token/login/', this.signInForm)
        console.log('SIGN IN RESPONSE', response)
        // if (response.status === 200) {
        //   throw new Error(response.status)
        // }
        this.$refs.signInForm.reset()
        localStorage.setItem('token', response.data.auth_token)
        this.$router.push('/settings')
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    }
  }
}
</script>
```

**URL** : `/auth/users/`

**Methods** : `POST`

Success Responses

**Code** : `201 Created`

**Content** : `{}`

```javascript
<script>
export default {
  name: 'SignUp',

  data: () => ({
    signUpForm: {
      first_name: '',
      last_name: '',
      passport: '',
      email: '',
      username: '',
      password: ''
    }
  }),

  methods: {
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
  }
}
</script>
```
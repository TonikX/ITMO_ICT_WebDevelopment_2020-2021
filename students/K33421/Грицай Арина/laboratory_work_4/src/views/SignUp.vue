<template>
  <div class="signup">
    <v-form
      @submit.prevent="signUp"
      ref="signUpForm"
      class="my-2"
    >
      <v-row>
        <v-col cols="3" class="mx-auto">
          <v-text-field
            label="Name"
            v-model="signUpForm.first_name"
          />
          <v-text-field
            label="Surname"
            v-model="signUpForm.last_name"
          />
          <v-text-field
            label="passport number"
            v-model="signUpForm.passport"
          />
          <v-text-field
            label="email"
            v-model="signUpForm.email"
          />
          <v-text-field
            label="login"
            v-model="signUpForm.username"
          />
          <v-text-field
            label="password"
            v-model="signUpForm.password"
            type="password"
          />
          <v-btn type="submit" color="gray" dark>Register</v-btn>

          <p class="mt-5">Already registred? <router-link to="/signin">Log In</router-link></p>
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>

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
        this.$router.push('/signin')
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    }
  }
}
</script>

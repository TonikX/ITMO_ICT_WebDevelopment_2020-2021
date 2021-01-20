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
            label="First name"
            v-model="signUpForm.first_name"
          />
          <v-text-field
            label="Last name"
            v-model="signUpForm.last_name"
          />
          <v-text-field
            label="Username"
            v-model="signUpForm.username"
          />
          <v-select
          v-model="signUpForm.role"
          :items="roles"
          item-text="role"
          item-value="role"
          label="Role"
          single-line
        ></v-select>
          <v-text-field
            label="Email"
            v-model="signUpForm.email"
          />
          <v-text-field
            label="Password"
            v-model="signUpForm.password"
            type="password"
          />
          <v-btn type="submit" dark>Register</v-btn>

          <p class="mt-5">Already have an account? <router-link to="/signin">Login</router-link></p>
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>

<script>
export default {
  name: 'SignUp',
  data: () => ({
    roles: ['s', 't', 'd'],
    signUpForm: {
      first_name: '',
      last_name: '',
      username: '',
      role: '',
      email: '',
      password: ''
    }
  }),
  methods: {
    async signUp () {
      try {
        const response = await this.axios
          .post('http://localhost:8000/auth/users/', this.signUpForm)
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

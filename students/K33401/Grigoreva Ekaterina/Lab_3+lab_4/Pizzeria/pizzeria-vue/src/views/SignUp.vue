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
            label="Enter username"
            v-model="signUpForm.username"
          />
          <v-text-field
            label="Enter first name"
            v-model="signUpForm.first_name"
          />
          <v-text-field
            label="Enter last name"
            v-model="signUpForm.last_name"
          />
          <v-text-field
            label="Enter date of birth"
            v-model="signUpForm.date_of_birth"
          />
          <v-text-field
            label="Enter address"
            v-model="signUpForm.address"
          />
          <v-text-field
            label="Enter password"
            v-model="signUpForm.password"
            type="password"
          />
          <v-btn type="submit" color="brown" dark>SignUp</v-btn>
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
      username: '',
      date_of_birth: '2000-01-01',
      address: '',
      password: '',
      first_name: '',
      last_name: ''
    }
  }),
  methods: {
    signUp () {
      try {
        this.axios.post('http://127.0.0.1:8000/auth/users/', this.signUpForm)
          .then(response => {
            if (response.status !== 201) {
              throw new Error(response.status)
            }
            this.$refs.signUpForm.reset()
            this.$router.push('/signin')
          })
        this.$refs.signUpForm.reset()
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    }
  }
}
</script>

<style scoped>

</style>

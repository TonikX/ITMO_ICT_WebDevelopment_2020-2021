<template>
  <v-container fluid>
    <v-layout row wrap>
      <v-flex xs12 class="text-xs-center" mt-14>
        <h1>Sign In</h1>
      </v-flex>
    <v-flex offset-md4 md4 mt-7 offset-sm2 sm8>
        <form @submit.prevent="login">
          <v-layout column>
            <v-flex>
              <v-text-field v-model="email" name="email"
                label="Email"
                type="email"
                required></v-text-field>
            </v-flex>
            <v-flex>
              <v-text-field v-model="password"
                name="password"
                label="Password"
                id="password"
                type="password"
                required></v-text-field>
            </v-flex>
            <v-flex class="text-xs-center" mt-5>
              <v-btn block outlined color="primary" type="submit">Sign In</v-btn>
            </v-flex>
          </v-layout>
        </form>
    </v-flex>
    </v-layout>
      <v-layout row wrap mt-7>
        <v-flex xs4 offset-xs4>
          <v-alert v-if="error" dense outlined type="error" mx-auto>
            {{ error }} 
          </v-alert>
        </v-flex>
      </v-layout>
  </v-container>
</template>


<script>


import DataService from "../../services/DataService"


export default {
  name: "Login",
  data() {
    return {
      email : "",
      password : "",
      error: null,
    }
  },
  components: {
  },
  methods: {
    login: function () {
        let email = this.email 
        let password = this.password
        DataService.login({
          email,
          password
        })
       .then((response) => {
         let token = response.data.auth_token
         console.log(token);

         return token;
       })
       .then(token => {
         localStorage.setItem('token', token)

         return token
       })
       .then(token => this.$store.dispatch('LOGIN', token) )
       .then(() => this.$router.push('/'))
       .catch(err => {
         this.error = err;
       })
      }
  }
}
</script>

<style>
  h1 {
    color: #37474F;
  } 
</style>

<!-- <form class="login" @submit.prevent="login">
     <h1>Sign in</h1>
     <label>Email</label>
     <input required v-model="email" type="email" placeholder="Name"/>
     <label>Password</label>
     <input required v-model="password" type="password" placeholder="Password"/>
     <hr/>
     <button type="submit">Login</button>
   </form> -->
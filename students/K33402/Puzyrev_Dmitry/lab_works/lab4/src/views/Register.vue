<template>
  <div class="container">
    <div class="row">
      <div class="col-md-4 offset-md-4 vh-100 d-flex flex-column justify-content-center">
        <h2 class="mb-5 text-center">Sign Up</h2>
        <form v-on:submit.prevent="registerUser">
          <div class="form-group">
            <label for="name">Name</label>
            <input type="text" class="form-control" id="name" v-model="name">
          </div>
          <div class="form-group">
            <label for="email">Email</label>
            <input type="email" class="form-control" id="email" v-model="email">
          </div>
          <div class="form-group">
            <label for="password">Password</label>
            <input type="password" class="form-control" id="password" v-model="pass">
          </div>
          <button type="submit" class="btn btn-danger btn-block">Sign Up</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Register",
  components: {},
  data() {
    return {
      name: '',
      email: '',
      pass: ''
    }
  },
  methods: {
    registerUser() {
      if (this.name && this.email && this.pass) {
        fetch('/api/register', {
            method: 'POST',
            body: JSON.stringify({name: this.name, email: this.email, pass: this.pass})
          })
            .then(response => response.json())
            .then(data => {
              if ('errors' in data) {
                alert('Email already exists!');
              } else {
                const answer = data['data']['createUser'];
                const myStorage = window.localStorage;
                myStorage.setItem('userId', answer['_id']);
                // myStorage.setItem('name', answer['name']);
                // myStorage.setItem('email', answer['email']);
                // myStorage.setItem('items', []);
                this.$router.push({ name: 'Account' })
              }
            })
            .catch(error => {
              console.log(error);
              alert('Error occured!');
            })


      }
    },
  }
  // mounted() {
  //   if (this.$route.params.option === 'signup') {
  //     this.title = 'Sign Up';
  //   } else {
  //     this.title = 'Login';
  //   }
  // }
}
</script>

<style lang="scss" scoped>
  
</style>
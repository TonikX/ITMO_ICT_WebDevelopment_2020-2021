<template>
  <div class="container">
    <div class="row">
      <div class="col-md-4 offset-md-4 vh-100 d-flex flex-column justify-content-center">
        <h2 class="mb-5 text-center">Login</h2>
        <form v-on:submit.prevent="loginUser">
          <div class="form-group">
            <label for="email">Email</label>
            <input type="email" class="form-control" id="email" v-model="email">
          </div>
          <div class="form-group">
            <label for="password">Password</label>
            <input type="password" class="form-control" id="password" v-model="pass">
          </div>
          <button type="submit" class="btn btn-danger btn-block">Login</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Hello",
  components: {},
  data() {
    return {
      email: '',
      pass: ''
    }
  },methods: {
    loginUser() {
      if (this.email && this.pass) {
        fetch('/api/login', {
            method: 'POST',
            body: JSON.stringify({email: this.email, pass: this.pass})
          })
            .then(response => response.json())
            .then(data => {
              if ('errors' in data) {
                alert('Wrong email or password!');
                console.log(data);
              } else {
                const answer = data['data']['loginUser'];
                const myStorage = window.localStorage;
                myStorage.setItem('userId', answer['_id']);
                // myStorage.setItem('name', answer['name']);
                // myStorage.setItem('email', answer['email']);
                // myStorage.setItem('items', answer['items'] ? answer['items'] : []);
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
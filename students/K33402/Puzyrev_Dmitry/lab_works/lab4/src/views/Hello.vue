<template>
  <div class="container">
    <div class="row">
      <div class="col vh-100 d-flex flex-column align-items-center justify-content-center text-center">
        <img src="../assets/img/list.svg" class="home-illustration" alt="">
        <!-- <h1 class="title is-size-1 mb-6">\ (•◡•) /</h1> -->
        <h4 class="subtitle mt-5 mb-5 text-center">Hi! This is simple app where you can create your wishist and share it with your friends. Let's create one!</h4>
        <div class="auth-buttons">
          <router-link :to="{ name: 'Register' }">
            <button class="btn btn-lg btn-danger mr-2">Sign Up</button>
          </router-link>
          <router-link :to="{ name: 'Login' }">
            <button class="btn btn-lg btn-outline-danger">Login</button>
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Hello",
  components: {},
}
</script>

<style lang="scss" scoped>
  .image {
    display: inline-block;
  }

  .subtitle {
    max-width: 400px;
    margin-left: auto;
    margin-right: auto;
    line-height: 1.25;
  }

  .auth-buttons {
    text-align: center; 
  }

  .home-illustration {
    max-width: 200px;
    display: inline-block;
    transform: rotate(10deg);

    &:hover {
      animation: animate_illustration 2s infinite;
    }
  }

  .btn {
    transition: background-color;
    transition-duration: .5s;
  }
  
  @keyframes animate_illustration {
    0% {
      transform: rotate(10deg);
    }
    50% {
      transform: rotate(-10deg);
    }
    100% {
      transform: rotate(10deg);
    }
  }
</style>
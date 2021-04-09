<template>
    <h1>Привет<span v-if="username">, {{ username }}</span>!</h1>
</template>

<script>
export default {
  name: 'GreetingCard',

  props: {
    username: String
  }
}
</script>

<style scoped>
  h1 {
    color: #42b983;
    margin: auto auto;
  }
</style>

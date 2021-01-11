<template>
  <section>
  <h1>Привет<span v-if="username">, {{ username }}</span>!</h1>
  </section>
</template>

<script>
export default {
  name: 'GreetingCard',

  props: {
    username: String,
    savedUsername: String
  }
}
</script>

<style>
.greeting-list li {
  text-align: left;
}
</style>

<template>
 <ul class="greeting-list">
   <li
     v-for="greeting in greetings"
     :key="greeting.id"
   >
     {{ greeting.text }}
   </li>
 </ul>
</template>

<script>
export default {
  name: 'GreetingList',
  data: () => ({
  }),

  props: {
    greetings: Array
  }
}
</script>

<style>
.greeting-list li {
 text-align: left;
}
</style>

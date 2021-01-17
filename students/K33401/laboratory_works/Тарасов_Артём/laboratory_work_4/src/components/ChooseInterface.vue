<template>
  <div>
    <router-link :to="{name:'Books'}">Книги</router-link>
    <router-link :to="{name:'Readers'}">Читателя</router-link>
  </div>
</template>

<script>
export default {
  name: 'ChooseInterface'
}
</script>

<style scoped>

</style>

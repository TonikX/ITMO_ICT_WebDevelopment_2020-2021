<template>
  <div>
    <router-link :to="{name:'Books'}">Книги</router-link> <br/>
    <router-link :to="{name:'Readers'}">Читатели</router-link> <br/>
    <router-link :to="{name:'InstancesOfBook'}">Экземпляр книги</router-link> <br/>
    <router-link :to="{name:'IssuingAInstances'}">Данные о выдаче</router-link> <br/>
  </div>
</template>

<script>

export default {
  name: 'ChooseInterface'
}
</script>

<style scoped>

</style>

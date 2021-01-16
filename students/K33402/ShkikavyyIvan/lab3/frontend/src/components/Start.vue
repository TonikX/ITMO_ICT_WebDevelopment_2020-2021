<template>
<div>
  <div class="block-round-content">
    <v-avatar size="300">
      <img src="https://upload.wikimedia.org/wikipedia/commons/8/85/Autoportrait_de_Vincent_van_Gogh.JPG">
    </v-avatar>
    <div align="center">
       <div class="label">Arthub</div>
       <div class="description">Место, где ты можешь высказать свое мнение о произведении искусства</div>
    </div>
  </div>
  <div class="block-round-content">
    <div align="center">
      <div class="description">SATOR AREPO TENET OPERA ROTAS</div>
      <v-btn class="button" @click="goHome">Поехали!</v-btn>
    </div>
    <v-avatar size="300">
      <img src="https://omskzdes.ru/storage/c/2019/06/04/1559649637_595439_65.jpg">
    </v-avatar>
  </div>
</div>
</template>

<script>
export default {
  name: 'Start',
  methods: {
    goHome () {
      this.$router.push({ name: 'Home' })
    }
  }
}
</script>

<style scoped>
.block-round-content {
  height: 65vh;
  display: flex;
  align-items: center;
  justify-content: space-around;
  background: #fff0b5; /* Цвет фона */
  padding: 10px; /* Поля вокруг текста */
}
.label{
  text-decoration: none;
  font-family: 'Lora', serif;
  font-style: normal;
  text-align: center;
  transition: .5s linear;
  width: 276px;
  font-size: 60px;
}
.description{
  text-decoration: none;
  font-family: 'Lora', serif;
  font-style: normal;
  text-align: center;
  transition: .5s linear;
  width: 252px;
  font-size:20px;
}
.button{
    color: #e0aa7c;
}
</style>

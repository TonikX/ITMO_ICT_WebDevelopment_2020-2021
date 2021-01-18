<template>
  <div class="row">
    <div class="row navigation">
      <div class="row navigation-row">
        <router-link to="/" class="nav">Главная</router-link>
        <router-link to="/prices" class="nav">Цены на абонементы</router-link>
        <router-link to="/timetable" class="nav">Расписание</router-link>
        <router-link to="/classes" class="nav">Групповые программы</router-link>
        <router-link to="/coaches" class="nav">Тренерский состав</router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'NavBar'
}
</script>

<style>
.navigation {
  width: 100%;
  height: 60px;
  background-color: black;
  margin-top: 5px;
  color: white;
  justify-content: center;
  align-items: center;
  margin-right: auto;
  margin-left: auto;
}
.navigation-row {
  width: 80%;
  justify-content: space-around;
}
.nav {
  color: white;
  text-decoration: none;
}
.nav:hover{
  text-decoration: none;
  color: white;
}
</style>

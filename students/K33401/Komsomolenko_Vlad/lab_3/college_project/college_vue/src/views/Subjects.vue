<template>
  <div class="table">
    <v-btn class="st_btn"
           href="/pairs"
    >
      <h4>Посмотреть пары</h4>
    </v-btn>
    <v-btn class="st_btn"
           href="/schedules"
    >
      <h4>Посмотреть расписания</h4>
    </v-btn>
    <v-btn class="st_btn"
           href="/paircreate"
    >
      <h4>Добавить новую пару</h4>
    </v-btn>
    <v-btn class="st_btn"
           href="/schedulecreate"
    >
      <h4>Сделать новое расписание</h4>
    </v-btn>
  </div>
</template>

<script>
export default {
  name: 'Subjects'
}
</script>

<style>
.table {
  margin: 3rem;
  width: 100%;
}
.st_btn {
  margin-left: 1rem;
  margin-right: 1rem;
  margin-bottom: 2rem;
  width: 40%;
}
</style>

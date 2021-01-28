<template>
  <div class="table">
    <v-btn class="st_btn"
           href="/createteacher"
    >
      <h4>Добавить нового преподавателя</h4>
    </v-btn>
    <v-btn class="st_btn"
           @click='push'
    >
      <h4>Изменить или удалить преподавателя</h4>
    </v-btn>
    <v-simple-table>
      <v-data-table-header>Список преподавателей</v-data-table-header>
      <tr>
        <td><strong>Имя</strong></td>
        <td><strong>Фамилия</strong></td>
        <td><strong>Аудитория</strong></td>
        <td><strong>Дисциплины</strong></td>
      </tr>
      <tr v-for="teacher in teachers" :key="teacher.id">
        <td>{{ teacher.firstname }}</td>
        <td>{{ teacher.lastname }}</td>
        <td>{{ teacher.room }}</td>
        <td>{{ teacher.discipline }}</td>
        <v-btn
          class="cr_del_btn"
          v-if="btn === true"
          @click="$router.push(`/updateteacher/${teacher.id}`)"
        >
          <h5>Изменить</h5>
        </v-btn>
        <v-btn
          color="red"
          class="cr_del_btn"
          v-if="btn === true"
          @click="delTr(teacher.id)"
        >
          <h5>Удалить</h5>
        </v-btn>
      </tr>
    </v-simple-table>
    <v-btn class="dis_btn"
           href="/creatediscipline"
    >
      <h4>Добавить новую дисциплину</h4>
    </v-btn>
  </div>
</template>

<script>
export default {
  name: 'Teacher',
  data: () => ({
    btn: false,
    teachers: [],
    disciplines: []
  }),
  async created () {
    await this.axios
      .get('http://127.0.0.1:8000/college/teachers/')
      .then((res) => {
        this.teachers = res.data
      })
      .catch((error) => {
        console.log(error)
      })
    await this.axios
      .get('http://127.0.0.1:8000/college/disciplines/')
      .then((res) => {
        this.disciplines = res.data
        for (const teacher of this.teachers) {
          const names = []
          for (const dis of teacher.discipline) {
            const nameId = dis - 1
            names.push(this.disciplines[nameId].title)
          }
          teacher.discipline = names
        }
      })
      .catch((error) => {
        console.log(error)
      })
  },
  methods: {
    async delTr (tr) {
      await this.axios
        .delete(`http://127.0.0.1:8000/college/teacher/updel/${tr}`)
        .then((res) => {
          console.log(res)
          this.$router.go()
        })
        .catch((error) => {
          console.log(error)
        })
    },
    async push () {
      this.btn = !this.btn
    }
  }
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
.cr_del_btn {
  margin: 1rem;
}
.dis_btn {
  margin: 3rem;
  width: 80%;
}
</style>

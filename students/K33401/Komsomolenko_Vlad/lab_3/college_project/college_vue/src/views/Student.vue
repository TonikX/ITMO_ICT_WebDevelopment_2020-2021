<template>
  <div class="table">
    <v-btn class="st_btn"
           href="/createstudent"
    >
      <h4>Добавить нового студента</h4>
    </v-btn>
    <v-btn class="st_btn"
           @click='push'
    >
      <h4>Изменить или удалить студента</h4>
    </v-btn>
    <v-simple-table>
      <v-data-table-header>Список студентов</v-data-table-header>
      <tr>
        <td><strong>Имя</strong></td>
        <td><strong>Фамилия</strong></td>
        <td><strong>Группа</strong></td>
      </tr>
      <tr v-for="student in students" :key="student.id">
        <td>{{ student.firstname }}</td>
        <td>{{ student.lastname }}</td>
        <td>{{ student.group }}</td>
        <v-btn
          class="cr_del_btn"
          v-if="btn === true"
          @click="$router.push(`/updatestudent/${student.id}`)"
        >
          <h5>Изменить</h5>
        </v-btn>
        <v-btn
          color="red"
          class="cr_del_btn"
          v-if="btn === true"
          @click="delSt(student.id)"
        >
          <h5>Удалить</h5>
        </v-btn>
      </tr>
    </v-simple-table>
  </div>
</template>

<script>
export default {
  name: 'Student',
  data: () => ({
    btn: false,
    students: []
  }),
  created () {
    this.axios
      .get('http://127.0.0.1:8000/college/students/')
      .then((res) => {
        this.students = res.data
      })
      .catch((error) => {
        console.log(error)
      })
  },
  methods: {
    async delSt (st) {
      await this.axios
        .delete(`http://127.0.0.1:8000/college/student/updel/${st}`)
        .then((res) => {
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
</style>

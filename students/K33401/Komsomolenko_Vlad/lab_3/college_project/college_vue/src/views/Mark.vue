<template>
  <div class="table">
    <v-btn class="st_btn"
           href="/markcreate"
    >
      <h4>Добавить новую оценку для студета</h4>
    </v-btn>
    <v-btn class="st_btn"
           @click='push'
    >
      <h4>Изменить оценку студента</h4>
    </v-btn>
    <v-simple-table
      v-if="btn === true"
    >
      <v-data-table-header>Список оценок</v-data-table-header>
      <tr>
        <td><strong>Студент</strong></td>
        <td><strong>Преподаватель</strong></td>
        <td><strong>Оценка</strong></td>
      </tr>
      <tr v-for="m in marks" :key="m.m_id">
        <td>{{ m.student }}</td>
        <td>{{ m.teacher }}</td>
        <td>{{ m.mark }}</td>
        <v-btn
          class="cr_del_btn"
          v-if="btn === true"
          @click="$router.push(`/updatemark/${m.m_id}`)"
        >
          <h5>Изменить</h5>
        </v-btn>
      </tr>
    </v-simple-table>
  </div>
</template>

<script>
export default {
  name: 'Mark',
  data: () => ({
    btn: false,
    students: [],
    teachers: [],
    marks: [],
    allMarks: []
  }),
  async created () {
    await this.axios
      .get('http://127.0.0.1:8000/college/marks')
      .then((res) => {
        this.allMarks = res.data
      })
      .catch((error) => {
        console.log(error)
      })
    await this.axios
      .get('http://127.0.0.1:8000/college/teachers')
      .then((res) => {
        this.teachers = res.data
      })
      .catch((error) => {
        console.log(error)
      })
    await this.axios
      .get('http://127.0.0.1:8000/college/students')
      .then((res) => {
        this.students = res.data
        const newMarks = []
        for (const st of this.students) {
          for (const mark of st.mark) {
            const m = {
              student: '',
              teacher: '',
              mark: '',
              m_id: ''
            }
            m.student = st.lastname
            const tID = this.allMarks[mark].teacher - 1
            console.log(this.allMarks[mark])
            const markID = mark
            m.teacher = this.teachers[tID].lastname
            m.mark = this.allMarks[markID].mark
            m.m_id = mark + 1
            newMarks.push(m)
          }
        }
        this.marks = newMarks
        console.log(newMarks)
      })
      .catch((error) => {
        console.log(error)
      })
  },
  methods: {
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

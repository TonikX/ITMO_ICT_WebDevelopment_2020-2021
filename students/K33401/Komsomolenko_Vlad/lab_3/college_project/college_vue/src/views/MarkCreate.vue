<template>
  <div>
    <v-form
      @submit.prevent="addMark"
      ref="form"
      class="my-2"
    >
      <v-row>
        <v-col cols="3" class="mx-auto">
          <v-select
            label="Выберете студента"
            v-model="form.student"
            :items="students"
            item-text="lastname"
            item-value="id"
            :reduce="option => option.code">
            <option v-for="st in students" :key="st.id">
              {{ st.lastname }}
            </option>
          </v-select>
          <v-select
            label="Выберете преподавателя"
            v-model="form.teacher"
            :items="teachers"
            item-text="lastname"
            item-value="id"
            :reduce="option => option.code">
            <option v-for="tr in teachers" :key="tr.id">
              {{ tr.lastname }}
            </option>
          </v-select>
          <v-text-field
            label="Добавьте оценку"
            v-model="form.mark"
          />
          <v-btn @click="addMark">Добавить</v-btn>
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>

<script>
export default {
  name: 'MarkCreate',
  data: () => ({
    students: [],
    teachers: [],
    upMarks: [],
    form: {
      mark: '',
      student: '',
      teacher: ''
    },
    newMark: {
      mark: '',
      teacher: ''
    },
    newStMark: {
      mark: '',
      student: ''
    }
  }),
  async created () {
    await this.axios
      .get('http://127.0.0.1:8000/college/students')
      .then((res) => {
        this.students = res.data
      })
      .catch((error) => {
        console.log(error)
      })
    await this.axios
      .get('http://127.0.0.1:8000/college/teachers')
      .then((res) => {
        this.teachers = res.data
        console.log(this.teachers)
      })
      .catch((error) => {
        console.log(error)
      })
  },
  methods: {
    async addMark () {
      this.newMark.mark = this.form.mark
      this.newMark.teacher = this.form.teacher
      await this.axios
        .post('http://127.0.0.1:8000/college/mark/create/', this.newMark)
        .then((res) => {
          console.log(res)
        })
        .catch((error) => {
          console.log(error)
        })
      await this.axios
        .get('http://127.0.0.1:8000/college/marks/')
        .then((res) => {
          this.newStMark.mark = res.data.length - 1
          this.newStMark.student = this.form.student
        })
        .catch((error) => {
          console.log(error)
        })
      await this.axios
        .post('http://127.0.0.1:8000/college/student/addmark/', this.newStMark)
        .then((res) => {
          console.log(res)
          window.location.href = '/marks'
        })
        .catch((error) => {
          console.log(error)
        })
    }
  }
}
</script>

<template>
  <div>
    <h1 class="title">Добавить новую дисциплину</h1>
    <v-form
      @submit.prevent="addDiscipline"
      ref="discipline"
      class="my-2"
    >
      <v-row>
        <v-col cols="3" class="mx-auto">
          <v-text-field
            label="Дисциплина"
            v-model="discipline.title"
          />
          <v-btn @click="addDiscipline">Добавить</v-btn>
        </v-col>
      </v-row>
    </v-form>
    <h1 class="title">Добавить новую дисциплину для преподавателя</h1>
    <v-form
      @submit.prevent="addDiscTeacher"
      ref="discTeacher"
      class="my-2"
    >
      <v-row>
        <v-col cols="3" class="mx-auto">
          <v-select
            label="Выберете дисциплину"
            v-model="discTeacher.discipline"
            :items="disciplines"
            item-text="title"
            item-value="id"
            :reduce="option => option.code">
            <option v-for="disc in disciplines" :key="disc.id">
              {{ disc.title }}
            </option>
          </v-select>
          <v-select
            label="Выберете преподавателя"
            v-model="discTeacher.teacher"
            :items="teachers"
            item-text="lastname"
            item-value="id"
            :reduce="option => option.code">
            <option v-for="tr in teachers" :key="tr.id">
              {{ tr.lastname }}
            </option>
          </v-select>
          <v-btn @click="addDiscTeacher">Добавить</v-btn>
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>

<script>
export default {
  name: 'DisciplineCreate',
  data: () => ({
    disciplines: [],
    teachers: [],
    discipline: {
      title: ''
    },
    discTeacher: {
      discipline: '',
      teacher: ''
    }
  }),
  async created () {
    await this.axios
      .get('http://127.0.0.1:8000/college/disciplines')
      .then((res) => {
        this.disciplines = res.data
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
  },
  methods: {
    async addDiscipline () {
      await this.axios
        .post('http://127.0.0.1:8000/college/discipline/create/', this.discipline)
        .then((res) => {
          console.log(res)
          window.location.href = ''
        })
        .catch((error) => {
          console.log(error)
        })
    },

    async addDiscTeacher () {
      await this.axios
        .post('http://127.0.0.1:8000/college/teacher/adddisc/', this.discTeacher)
        .then((res) => {
          console.log(res)
          window.location.href = ''
        })
        .catch((error) => {
          console.log(error)
        })
    }
  }
}
</script>
<style>
.title {
  padding: 3rem;
}
</style>

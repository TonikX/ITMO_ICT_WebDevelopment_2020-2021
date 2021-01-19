<template>
  <div>
    <v-form
      @submit.prevent="addTeacher"
      ref="teacher"
      class="my-2"
    >
      <v-row>
        <v-col cols="3" class="mx-auto">
          <v-text-field
            label="Имя"
            v-model="teacher.firstname"
          />
          <v-text-field
            label="Фамилия"
            v-model="teacher.lastname"
          />
          <v-text-field
            label="Аудитория"
            v-model="teacher.room"
          />
          <v-btn @click="addTeacher">Добавить</v-btn>
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>

<script>
export default {
  name: 'TeacherCreate',
  data: () => ({
    teacher: {
      firstname: '',
      lastname: '',
      room: ''
    }
  }),
  methods: {
    async addTeacher () {
      await this.axios
        .post('http://127.0.0.1:8000/college/teacher/create/', this.teacher)
        .then((res) => {
          console.log(res)
          window.location.href = '/teachers'
        })
        .catch((error) => {
          console.log(error)
        })
    }
  }
}
</script>

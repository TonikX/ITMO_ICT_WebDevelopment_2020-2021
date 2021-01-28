<template>
  <div>
    <v-form
      @submit.prevent="addStudent"
      ref="student"
      class="my-2"
    >
      <v-row>
        <v-col cols="3" class="mx-auto">
          <v-text-field
            label="Имя"
            v-model="student.firstname"
          />
          <v-text-field
            label="Фамилия"
            v-model="student.lastname"
          />
          <v-text-field
            label="Группа"
            v-model="student.group"
          />
          <v-btn @click="addStudent">Добавить</v-btn>
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>

<script>
export default {
  name: 'StudentCreate',
  data: () => ({
    student: {
      firstname: '',
      lastname: '',
      group: ''
    }
  }),
  methods: {
    async addStudent () {
      await this.axios
        .post('http://127.0.0.1:8000/college/student/create/', this.student)
        .then((res) => {
          console.log(res)
          window.location.href = '/students'
        })
        .catch((error) => {
          console.log(error)
        })
    }
  }
}
</script>

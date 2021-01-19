<template>
  <div>
    <v-form
      @submit.prevent="update"
      ref="newSt"
      class="my-2"
    >
      <v-row>
        <v-col cols="4" class="mx-auto">
          <v-text-field
            label="Измените имя"
            item-text = 'this.st_cur.group'
            v-model="newSt.firstname"
          />
          <v-text-field
            label="Измените фамилию"
            v-model="newSt.lastname"
          />
          <v-text-field
            label="Измените группу"
            v-model="newSt.group"
          />
          <v-btn @click="update">Обновить</v-btn>
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>

<script>
export default {
  name: 'UpdateStudent',
  data: () => ({
    st_id: 0,
    st_cur: {},
    newSt: {
      firstname: '',
      lastname: '',
      group: ''
    }
  }),
  created () {
    this.st_id = this.$route.params.student_id
    this.axios
      .get(`http://127.0.0.1:8000/college/student/updel/${this.st_id}`)
      .then((res) => {
        this.st_cur = res.data
        this.newSt.lastname = this.st_cur.lastname
        this.newSt.firstname = this.st_cur.firstname
        this.newSt.group = this.st_cur.group
        console.log(this.st_cur)
      })
  },
  methods: {
    async update () {
      await this.axios
        .put(`http://127.0.0.1:8000/college/student/updel/${this.st_id}`, this.newSt)
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

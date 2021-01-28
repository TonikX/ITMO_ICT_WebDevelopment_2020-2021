<template>
  <div>
    <v-form
      @submit.prevent="update"
      ref="newTr"
      class="my-2"
    >
      <v-row>
        <v-col cols="4" class="mx-auto">
          <v-text-field
            label="Измените имя"
            item-text = 'this.tr_cur.group'
            v-model="newTr.firstname"
          />
          <v-text-field
            label="Измените фамилию"
            v-model="newTr.lastname"
          />
          <v-text-field
            label="Измените аудиторию"
            v-model="newTr.room"
          />
          <v-btn @click="update">Обновить</v-btn>
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>

<script>
export default {
  name: 'UpdateTeacher',
  data: () => ({
    tr_id: 0,
    tr_cur: {},
    newTr: {
      firstname: '',
      lastname: '',
      room: ''
    }
  }),
  created () {
    this.tr_id = this.$route.params.teacher_id
    this.axios
      .get(`http://127.0.0.1:8000/college/teacher/updel/${this.tr_id}`)
      .then((res) => {
        this.tr_cur = res.data
        this.newTr.lastname = this.tr_cur.lastname
        this.newTr.firstname = this.tr_cur.firstname
        this.newTr.room = this.tr_cur.room
        console.log(this.tr_cur)
      })
  },
  methods: {
    async update () {
      await this.axios
        .put(`http://127.0.0.1:8000/college/teacher/updel/${this.tr_id}`, this.newTr)
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

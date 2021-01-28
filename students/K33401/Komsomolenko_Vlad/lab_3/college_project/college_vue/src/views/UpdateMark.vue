<template>
  <div>
    <v-form
      @submit.prevent="update"
      ref="mark"
      class="my-2"
    >
      <v-row>
        <v-col cols="4" class="mx-auto">
          <v-text-field
            label="Измените оценку"
            v-model="mark.mark"
          />
          <v-select
            label="Измените преподавателя"
            v-model="mark.teacher"
            :items="teachers"
            item-text="lastname"
            item-value="id"
            :reduce="option => option.code">
            <option v-for="tr in teachers" :key="tr.id">
              {{ tr.lastname }}
            </option>
          </v-select>
          <v-btn @click="update">Обновить</v-btn>
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>

<script>
export default {
  name: 'UpdateMark',
  data: () => ({
    mark_id: 0,
    teachers: [],
    mark_cur: {},
    mark: {
      mark: '',
      teacher: ''
    }
  }),
  async created () {
    this.mark_id = this.$route.params.mark_id
    await this.axios
      .get('http://127.0.0.1:8000/college/teachers')
      .then((res) => {
        this.teachers = res.data
        console.log(this.teachers)
      })
      .catch((error) => {
        console.log(error)
      })
    await this.axios
      .get(`http://127.0.0.1:8000/college/mark/updel/${this.mark_id}`)
      .then((res) => {
        this.mark_cur = res.data
        this.mark.mark = this.mark_cur.mark
        this.mark.teacher = this.mark_cur.teacher
      })
  },
  methods: {
    async update () {
      await this.axios
        .put(`http://127.0.0.1:8000/college/mark/updel/${this.mark_id}`, this.mark)
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

<template>
  <div class="add">
    <div><v-btn small @click='$router.go(-1)'>Back</v-btn></div>
    <v-form
      @submit.prevent="update"
      ref="addForm"
      class="my-2"
    >
      <v-row>
        <v-col cols="4" class="mx-auto">
          <v-text-field
            label="Enter first_name"
            item-text = 'this.st_cur.group'
            v-model="addForm.first_name"
          />
          <v-text-field
            label="Enter last_name"
            v-model="addForm.last_name"
          />
          <v-text-field
            label="Enter group"
            v-model="addForm.group"
          />
          <v-btn color="primary" @click="update">update</v-btn>
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>

<script>
export default {
  name: 'StudentEdit',
  data: () => ({
    st_id: 0,
    st_cur: {},
    addForm: {
      first_name: '',
      last_name: '',
      group: ''
    }
  }),
  created () {
    this.st_id = this.$route.params.student_id
    this.axios
      .get(`http://127.0.0.1:8000/student/${this.st_id}`)
      .then((res) => {
        console.log(res)
        this.st_cur = res.data
        this.addForm.last_name = this.st_cur.last_name
        this.addForm.first_name = this.st_cur.first_name
        this.addForm.group = this.st_cur.group
        console.log(this.st_cur)
      })
  },
  methods: {
    async update () {
      await this.axios
        .put(`http://127.0.0.1:8000/student/${this.st_id}/`, this.addForm)
        .then((res) => {
          console.log(res)
          this.$refs.addForm.reset()
          this.$router.go(0)
        })
        .catch((error) => {
          console.log(error)
        })
    }
  }
}
</script>

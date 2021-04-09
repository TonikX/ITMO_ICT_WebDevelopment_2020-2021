<template>
  <div class="add">
    <div><v-btn small @click='$router.go(-1)'>Back</v-btn></div>
    <v-form
      @submit.prevent="add"
      ref="addForm"
      class="my-2"
    >
      <v-row>
        <v-col cols="3" class="mx-auto">
          <v-text-field
            label="Enter first_name"
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
          <v-btn color="primary" @click="add">add</v-btn>
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>

<script>
export default {
  name: 'StudentCreate',
  data: () => ({
    addForm: {
      first_name: '',
      last_name: '',
      group: ''
    }
  }),
  methods: {
    async add () {
      await this.axios
        .post('http://127.0.0.1:8000/student/create/', this.addForm)
        .then((res) => {
          console.log(res)
          this.$refs.addForm.reset()
        })
        .catch((error) => {
          console.log(error)
        })
    }
  }
}
</script>

<template>
  <div class="add">
    <div><v-btn small @click='$router.go(-1)'>Back</v-btn></div>
    <v-form
      @submit.prevent="add"
      ref="addForm"
      class="my-2"
    >
      <v-row>
        <v-col cols="5" class="mx-auto">
          <v-text-field
            label="Введите фамилию"
            v-model="addForm.last_name"
          />
          <v-text-field
            label="Введите имя"
            v-model="addForm.first_name"
          />
          <v-text-field
            label="Введите отчество"
            v-model="addForm.middle_name"
          />
          <v-select
            label="Выберите дни уборки"
            v-model="addParams.params"
            multiple="multiple"
            :items="params"
            item-text="label"
            item-value="code">
            <option v-for="param in params" :key="param.id">
              {{ param.label }}
            </option>
          </v-select>
          <v-btn color="primary" @click="add">add</v-btn>
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>

<script>
export default {
  name: 'StaffCreate',
  data: () => ({
    staff_id: '',
    params: [],
    addForm: {
      first_name: '',
      last_name: '',
      middle_name: ''
    },
    addParams: {
      params: []
    }
  }),
  created () {
    this.axios
      .get('http://127.0.0.1:8000/cleaning_params/list/')
      .then((res) => {
        const data = res.data
        console.log(res.data)
        for (let i = 0; i < res.data.length; i++) {
          const label = `${data[i].day} ${data[i].floor} `
          const id = data[i].id
          this.params.push({ label: label, code: id })
        }
      })
      .catch((error) => {
        console.log(error)
      })
  },
  methods: {
    async add () {
      await this.axios
        .post('http://127.0.0.1:8000/staff/create/', this.addForm)
        .then((res) => {
          console.log(res)
        })
        .catch((error) => {
          console.log(error)
        })
      await this.axios
        .get('http://127.0.0.1:8000/staff/list/')
        .then((res) => {
          this.staff_id = res.data[res.data.length - 1].id
        })
        .catch((error) => {
          console.log(error)
        })
      for (const param of this.addParams.params) {
        await this.axios
          .post('http://127.0.0.1:8000/staff_cleaning/create/', {
            staff: this.staff_id,
            params: param
          })
          .then((res) => {
            console.log(res)
          })
          .catch((error) => {
            console.log(error)
          })
      }
      this.$refs.addForm.reset()
    }
  }
}
</script>

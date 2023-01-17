<template>
  <div class="add">
    <div><v-btn small @click='$router.go(-1)'>Back</v-btn></div>
    <v-row>
      <v-col class="col" cols="4">
        <table>
          <tr>
            <td><strong>Имя</strong></td>
            <td>{{ cur.first_name }}</td>
          </tr>
          <tr>
            <td><strong>Фамилия</strong></td>
            <td>{{ cur.last_name }}</td>
          </tr>
          <tr>
            <td><strong>Отчество</strong></td>
            <td>{{ cur.middle_name }}</td>
          </tr>
          <tr>
            <td><strong>Расписание уборки</strong></td>
            <td>
              <p v-for="el in cur.cleaning" :key="el.day">
                {{ el.day }}
                {{ el.floor }}
              </p>
            </td>
          </tr>
        </table>
      </v-col>
      <v-col class="col" cols="4">
        <v-form
          @submit.prevent="update"
          ref="addForm"
          class="my-2"
        >
          <v-row>
            <v-col cols="5" class="mx-auto">
              <v-text-field
                label="Введите номер паспорта"
                v-model="addForm.first_name"
              />
              <v-text-field
                label="Введите фамилию"
                v-model="addForm.last_name"
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
              <v-btn color="primary" @click="update">update</v-btn>
            </v-col>
          </v-row>
        </v-form>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  name: 'StaffDetail',
  data: () => ({
    cur_id: 0,
    cur: {},
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
    this.cur_id = this.$route.params.staff_id
    this.axios
      .get(`http://127.0.0.1:8000/staff/${this.cur_id}`)
      .then((res) => {
        this.cur = res.data
        this.addForm.last_name = this.cur.last_name
        this.addForm.first_name = this.cur.first_name
        this.addForm.middle_name = this.cur.middle_name
        for (let i = 0; i < this.cur.cleaning.length; i++) {
          this.addParams.params.push(this.cur.cleaning[i])
        }
      })
    this.axios
      .get('http://127.0.0.1:8000/cleaning_params/list')
      .then((res) => {
        console.log(res.data)
        const data = res.data
        for (let i = 0; i < res.data.length; i++) {
          const label = `${data[i].day} ${data[i].floor} `
          const id = data[i].id
          this.params.push({ label: label, code: id })
        }
      })
  },
  methods: {
    async update () {
      await this.axios
        .put(`http://127.0.0.1:8000/staff/${this.cur_id}/`, this.addForm)
        .then((res) => {
          console.log(res)
        })
        .catch((error) => {
          console.log(error)
          alert('Введены некоректные данные!')
        })
      for (const param of this.cur.cleaning) {
        const id = await this.axios
          .get('http://127.0.0.1:8000/staff_cleaning/list/')
          .then((res) => {
            console.log(res.data)
            return res.data.filter(val => val.staff.toString() === this.cur_id && val.params === param.id)[0].id
          })
          .catch((error) => {
            console.log(error)
          })
        await this.axios
          .delete(`http://127.0.0.1:8000/staff_cleaning/${id}/`)
          .then((res) => {
            console.log(res)
          })
          .catch((error) => {
            console.log(error)
          })
      }
      for (const param of this.addParams.params) {
        await this.axios
          .post('http://127.0.0.1:8000/staff_cleaning/create/', {
            staff: this.cur_id,
            params: param
          })
          .then((res) => {
            console.log(res)
          })
          .catch((error) => {
            console.log(error)
          })
      }
      window.location.href = `http://localhost:8080/staff/${this.cur_id}`
    }
  }
}
</script>

<style scoped>
  .col {
    margin: 10px;
  }
  table {
    margin-top: 30px;
    width: 100%;
  }
  td {
    padding: 0.5rem;
    border-bottom: 1px solid black;
  }
  button {
    margin: 10px;
  }
</style>

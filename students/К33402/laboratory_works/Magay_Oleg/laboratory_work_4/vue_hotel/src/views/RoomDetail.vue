<template>
  <div class="add">
    <div><v-btn small @click='$router.go(-1)'>Back</v-btn></div>
    <v-row>
      <v-col class="col" cols="4">
        <table>
          <tr>
            <td><strong>Номер</strong></td>
            <td>{{ cur.number }}</td>
          </tr>
          <tr>
            <td><strong>Телефон</strong></td>
            <td>{{ cur.phone }}</td>
          </tr>
          <tr>
            <td><strong>Цена</strong></td>
            <td>{{ cur.price }}</td>
          </tr>
          <tr>
            <td><strong>Статус</strong></td>
            <td>{{ cur.status }}</td>
          </tr>
          <tr>
            <td><strong>Прибыль с номера</strong></td>
            <td>{{ cur.total }}</td>
          </tr>
          <tr>
            <td><strong>Тип</strong></td>
            <td>{{ cur.type }}</td>
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
                label="Введите номер"
                v-model="addForm.number"
              />
              <v-text-field
                label="Введите телефон"
                v-model="addForm.phone"
              />
              <v-text-field
                label="Введите цену"
                v-model="addForm.price"
              />
              <v-select
                label="Выберите статус"
                v-model="addForm.status"
                :items="opts"
                item-text="label"
                item-value="code">
                <option v-for="opt in opts" :key="opt.id">
                  {{ opt.label }}
                </option>
              </v-select>
              <v-text-field
                label="Введите прибыль с номера"
                v-model="addForm.total"
              />
              <v-select
                label="Выберите тип"
                v-model="addForm.type"
                :items="types"
                item-text="label"
                item-value="code">
                <option v-for="type in types" :key="type.id">
                  {{ type.label }}
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
  name: 'RoomDetail',
  data: () => ({
    cur_id: 0,
    cur: {},
    opts: [{ label: 'свободно', code: 'free' }, { label: 'занято', code: 'busy' }],
    types: [{ label: 'одноместный', code: 'one' }, { label: 'двуместный', code: 'two' }, { label: 'трехместный', code: 'three' }],
    addForm: {
      number: '',
      phone: '',
      price: '',
      status: '',
      total: 0,
      type: ''
    }
  }),
  created () {
    this.cur_id = this.$route.params.room_id
    this.axios
      .get(`http://127.0.0.1:8000/room/${this.cur_id}`)
      .then((res) => {
        this.cur = res.data
        this.addForm.number = this.cur.number
        this.addForm.phone = this.cur.phone
        this.addForm.price = this.cur.price
        this.addForm.status = this.cur.status
        this.addForm.total = this.cur.total
        this.addForm.type = this.cur.type
        console.log(this.cur)
      })
  },
  methods: {
    async update () {
      await this.axios
        .put(`http://127.0.0.1:8000/room/${this.cur_id}/`, this.addForm)
        .then((res) => {
          console.log(res)
        })
        .catch((error) => {
          console.log(error)
          alert('Введены некоректные данные!')
        })
      this.$refs.addForm.reset()
      window.location.href = `http://localhost:8080/room/${this.cur_id}`
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
</style>

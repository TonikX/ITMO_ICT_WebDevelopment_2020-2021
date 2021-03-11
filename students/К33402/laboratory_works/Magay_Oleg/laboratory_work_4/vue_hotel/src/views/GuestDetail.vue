<template>
  <div class="add">
    <div><v-btn small @click='$router.go(-1)'>Back</v-btn></div>
    <v-row>
    <v-col class="col" cols="4">
      <table>
        <tr>
          <td><strong>Номер паспорта</strong></td>
          <td>{{ cur.passport }}</td>
        </tr>
        <tr>
          <td><strong>Фамилия</strong></td>
          <td>{{ cur.last_name }}</td>
        </tr>
        <tr>
          <td><strong>Имя</strong></td>
          <td>{{ cur.first_name }}</td>
        </tr>
        <tr>
          <td><strong>Отчество</strong></td>
          <td>{{ cur.middle_name }}</td>
        </tr>
        <tr>
          <td><strong>Город</strong></td>
          <td>{{ cur.city }}</td>
        </tr>
        <tr>
          <td><strong>Дата заселения</strong></td>
          <td>{{ cur.start_date }}</td>
        </tr>
        <tr>
          <td><strong>Номер</strong></td>
          <td>{{ room.number }}</td>
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
            v-model="addForm.passport"
          />
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
          <v-text-field
            label="Введите ваш город"
            v-model="addForm.city"
          />
          <v-text-field
            label="Выберите дату заселения"
            v-model="addForm.start_date"
            type="date"
          />
          <v-select
            label="Выберите номер"
            v-model="addForm.room"
            :items="rooms"
            item-text="number"
            item-value="id"
            :reduce="option => option.code">
            <option v-for="room in rooms" :key="room.id">
              {{ room.number }}
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
  name: 'GuestDetail',
  data: () => ({
    cur_id: 0,
    cur: {},
    rooms: [],
    room: {
      number: ''
    },
    next_room: {},
    addForm: {
      first_name: '',
      last_name: '',
      middle_name: '',
      passport: '',
      city: '',
      start_date: '',
      room: ''
    }
  }),
  created () {
    this.room.number = ' '
    this.cur_id = this.$route.params.guest_id
    this.axios
      .get(`http://127.0.0.1:8000/guest/${this.cur_id}`)
      .then((res) => {
        this.cur = res.data
        this.addForm.last_name = this.cur.last_name
        this.addForm.first_name = this.cur.first_name
        this.addForm.middle_name = this.cur.middle_name
        this.addForm.room = this.cur.room
        this.addForm.start_date = this.cur.start_date
        this.addForm.city = this.cur.city
        this.addForm.passport = this.cur.passport
        console.log(this.cur)
      })
    this.axios
      .get('http://127.0.0.1:8000/room/list')
      .then((res) => {
        console.log(res.data)
        this.rooms = res.data.filter(val => val.status === 'free' || val.id === this.cur.room)
        this.room = res.data.filter(val => val.id === this.cur.room)[0]
        console.log('this.room', this.room)
      })
  },
  methods: {
    async update () {
      await this.axios
        .put(`http://127.0.0.1:8000/guest/${this.cur_id}/`, this.addForm)
        .then((res) => {
          console.log(res)
        })
        .catch((error) => {
          console.log(error)
          alert('Введены некоректные данные!')
        })
      await this.axios
        .get(`http://127.0.0.1:8000/room/${this.addForm.room}/`)
        .then((res) => {
          console.log(res.data)
          this.next_room = res.data
        })
        .catch((error) => {
          console.log(error)
        })
      this.room.status = 'free'
      await this.axios
        .put(`http://127.0.0.1:8000/room/${this.cur.room}/`, this.room)
        .then((res) => {
          console.log(res.data)
        })
        .catch((error) => {
          console.log(error)
        })
      this.next_room.status = 'busy'
      await this.axios
        .put(`http://127.0.0.1:8000/room/${this.addForm.room}/`, this.next_room)
        .then((res) => {
          console.log(res.data)
        })
        .catch((error) => {
          console.log(error)
        })
      console.log('this.room', this.room, 'next', this.next_room)
      this.$refs.addForm.reset()
      window.location.href = `http://localhost:8080/guest/${this.cur_id}`
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

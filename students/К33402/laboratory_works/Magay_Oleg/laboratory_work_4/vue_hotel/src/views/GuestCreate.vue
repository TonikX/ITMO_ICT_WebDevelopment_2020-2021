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
            item-value="id">
            <option v-for="room in rooms" :key="room.id">
              {{ room.number }}
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
  name: 'GuestCreate',
  data: () => ({
    rooms: [],
    next_room: '',
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
    this.axios
      .get('http://127.0.0.1:8000/room/list')
      .then((res) => {
        console.log(res.data)
        this.rooms = res.data.filter(val => val.status === 'free')
        console.log('this.rooms', this.rooms)
      })
  },
  methods: {
    async add () {
      await this.axios
        .post('http://127.0.0.1:8000/guest/create/', this.addForm)
        .then((res) => {
          console.log(res)
        })
        .catch((error) => {
          console.log(error)
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
      this.next_room.status = 'busy'
      await this.axios
        .put(`http://127.0.0.1:8000/room/${this.addForm.room}/`, this.next_room)
        .then((res) => {
          console.log(res.data)
        })
        .catch((error) => {
          console.log(error)
        })
      this.$refs.addForm.reset()
    }
  }
}
</script>

<template>
  <div class="home">
    <div v-if="!isAuth">
      <h3>Данные доступны только авторизованным пользователям. Пожалуйста, войдите или зарегистрируйтесь!</h3>
    </div>
    <div v-if="isAuth">
      <h3>Список гостей отеля</h3>
      <v-btn small @click="$router.push('/guest/create')">Новый гость</v-btn>
      <v-simple-table>
        <tr>
          <td><strong>Фамилия</strong></td>
          <td><strong>Имя</strong></td>
          <td></td>
        </tr>
        <tr v-for="guest in guests" :key="guest.id">
          <td>{{ guest.first_name }}</td>
          <td>{{ guest.last_name }}</td>
          <td>
            <v-btn small @click='$router.push(`/guest/${ guest.id }`)'>Detail</v-btn>
            <v-btn small color="error" @click="deleteElem(guest.id, guest.room)">delete</v-btn>
          </td>
        </tr>
      </v-simple-table>
    </div>
  </div>
</template>

<script>

export default {
  name: 'Home',
  data: () => ({
    guests: [],
    room: '',
    isAuth: ''
  }),
  created () {
    this.isAuth = localStorage.getItem('token') !== null && localStorage.getItem('token') !== undefined
    this.axios
      .get('http://127.0.0.1:8000/guest/list/')
      .then((res) => {
        this.guests = res.data
      })
      .catch((error) => {
        console.log(error)
      })
  },
  methods: {
    async deleteElem (id, room) {
      await this.axios
        .delete(`http://127.0.0.1:8000/guest/${id}`)
        .then((res) => {
          console.log(res)
        })
        .catch((error) => {
          console.log(error)
        })
      await this.axios
        .get(`http://127.0.0.1:8000/room/${room}`)
        .then((res) => {
          this.room = res.data
          console.log('this.room', this.room)
        })
      this.room.total = this.room.total + this.room.price
      this.room.status = 'free'
      await this.axios
        .put(`http://127.0.0.1:8000/room/${room}/`, this.room)
        .then((res) => {
          console.log(res.data)
        })
        .catch((error) => {
          console.log(error)
        })
      this.$router.go(0)
    }
  }
}
</script>

<style scoped>
  table {
    margin-top: 50px;
    width: 100%;
  }
  td {
    text-align: left;
    padding: 0.5rem;
  }
  button {
    margin: 10px;
  }
</style>

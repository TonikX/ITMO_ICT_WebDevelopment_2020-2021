<template>
  <div class="home">
    <h3>Список номеров отеля</h3>
    <v-btn small @click='$router.push("/room/create")'>Новый номер</v-btn>
    <table>
      <tr>
        <td><strong>Номер</strong></td>
        <td><strong>Тип</strong></td>
        <td><strong>Цена</strong></td>
        <td><strong>Статус</strong></td>
        <td></td>
      </tr>
      <tr v-for="room in rooms" :key="room.id">
        <td>{{ room.number }}</td>
        <td>{{ room.type }}</td>
        <td>{{ room.price }}</td>
        <td>{{ room.status }}</td>
        <td>
          <v-btn small @click='$router.push(`/room/${ room.id }`)'>Detail</v-btn>
          <v-btn small color="error" @click="deleteElem(room.id)" style="margin-right: 20px">delete</v-btn>
        </td>
      </tr>
    </table>
  </div>
</template>

<script>
export default {
  name: 'Room',
  data: () => ({
    rooms: []
  }),
  created () {
    this.axios
      .get('http://127.0.0.1:8000/room/list/')
      .then((res) => {
        this.rooms = res.data
      })
      .catch((error) => {
        console.log(error)
      })
  },
  methods: {
    async deleteElem (el) {
      await this.axios
        .delete(`http://127.0.0.1:8000/room/${el}`)
        .then((res) => {
          console.log(res)
          this.$router.go()
        })
        .catch((error) => {
          console.log(error)
        })
    }
  }
}
</script>

<style scoped>
  table {
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

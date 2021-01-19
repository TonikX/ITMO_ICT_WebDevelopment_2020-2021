<template>
  <div class="home">
    <h3>Список персонала отеля</h3>
    <v-btn small @click="$router.push('/staff/create')">Новый сотрудник</v-btn>
    <table>
      <tr>
        <td><strong>Фамилия</strong></td>
        <td><strong>Имя</strong></td>
        <td></td>
      </tr>
      <tr v-for="staff_ in staff" :key="staff_.id">
        <td>{{ staff_.first_name }}</td>
        <td>{{ staff_.last_name }}</td>
        <td>
          <v-btn small @click='$router.push(`/staff/${ staff_.id }`)'>Detail</v-btn>
          <v-btn small color="error" @click="deleteElem(staff_.id)" style="margin-right: 20px">delete</v-btn></td>
      </tr>
    </table>
  </div>
</template>

<script>
export default {
  name: 'staff_',
  data: () => ({
    staff: []
  }),
  created () {
    this.axios
      .get('http://127.0.0.1:8000/staff/list/')
      .then((res) => {
        this.staff = res.data
      })
      .catch((error) => {
        console.log(error)
      })
  },
  methods: {
    async deleteElem (el) {
      await this.axios
        .delete(`http://127.0.0.1:8000/staff/${el}`)
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

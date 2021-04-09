<template>
  <div>
    <h2>Schedule</h2>
    <v-btn class="btn" small @click="$router.push('/pair/create')">Pair Create</v-btn>
    <v-simple-table>
      <v-data-table-header>pairs</v-data-table-header>
      <tr>
        <td><strong>group</strong></td>
        <td><strong>pair_number</strong></td>
        <td><strong>name_day</strong></td>
        <td><strong>room</strong></td>
        <td><strong>teacher</strong></td>
        <td><strong>subject</strong></td>
        <td></td>
        <td></td>
      </tr>
      <tr v-for="el in elems" :key="el.id">
        <td>{{ el.group }}</td>
        <td>{{ el.pair_number }}</td>
        <td>{{ el.name_day }}</td>
        <td>{{ el.room }}</td>
        <td>{{ el.teacher }}</td>
        <td>{{ el.subject }}</td>
        <td><v-btn small @click='$router.push(`/pair/${ el.id }`)'>Edit</v-btn></td>
        <td><v-btn small color="error" @click="deleteElem(el.id)" style="margin-right: 20px">delete</v-btn></td>
      </tr>
    </v-simple-table>
  </div>
</template>

<script>
export default {
  name: 'HomeManager',
  data: () => ({
    pairs: [],
    teachers: [],
    subjects: [],
    elems: []
  }),
  async created () {
    await this.axios
      .get('http://127.0.0.1:8000/pair/list/')
      .then((res) => {
        this.pairs = res.data
      })
      .catch((error) => {
        console.log(error)
      })
    await this.axios
      .get('http://127.0.0.1:8000/teacher/list/')
      .then((res) => {
        this.teachers = res.data
      })
      .catch((error) => {
        console.log(error)
      })
    await this.axios
      .get('http://127.0.0.1:8000/subject/list/')
      .then((res) => {
        this.subjects = res.data
      })
      .catch((error) => {
        console.log(error)
      })
    for (const i of this.pairs) {
      const tea = this.teachers.filter(val => val.id === i.teacher)[0]
      const sub = this.subjects.filter(val => val.id === i.subject)[0]
      this.elems.push({ id: i.id, pair_number: i.pair_number, name_day: i.name_day, room: i.room, group: i.group, subject: sub.name, teacher: `${tea.first_name} ${tea.last_name}` })
    }
  },
  methods: {
    async deleteElem (elem) {
      await this.axios
        .delete(`http://127.0.0.1:8000/pair/${elem}`)
        .then((res) => {
          console.log(res)
          this.$router.go(0)
        })
        .catch((error) => {
          console.log(error)
        })
    }
  }
}
</script>

<style>
  table {
    margin-top: 50px;
    width: 100%;
  }
  td {
    text-align: left;
    padding: 0.5rem;
  }
  .btn {
    margin-top: 10px;
  }
</style>

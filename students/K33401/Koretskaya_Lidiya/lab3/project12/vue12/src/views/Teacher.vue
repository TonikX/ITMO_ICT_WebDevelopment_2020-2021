<template>
  <div>
    <div><v-btn small @click='$router.go(-1)'>Back</v-btn></div>
    <v-simple-table>
      <v-data-table-header>teachers</v-data-table-header>
      <tr>
        <td><strong>first_name</strong></td>
        <td><strong>last_name</strong></td>
        <td><strong>subject</strong></td>
        <td><strong>room</strong></td>
        <td></td>
        <td></td>
      </tr>
      <tr v-for="el in teachers" :key="el.id">
        <td>{{ el.first_name }}</td>
        <td>{{ el.last_name }}</td>
        <td><i v-for="sub in el.subjects" :key="sub.name">{{ sub.name }} </i></td>
        <td v-if="el.room">{{ el.room }}</td>
        <td v-else> - </td>
        <td><v-btn small @click='$router.push(`/teacher/${ el.id }`)'>Edit</v-btn></td>
        <td><v-btn small color="error" @click="deleteElem(el.id)" style="margin-right: 20px">delete</v-btn></td>
      </tr>
    </v-simple-table>
  </div>
</template>

<script>
export default {
  name: 'TeacherCreate',
  data: () => ({
    teachers: []
  }),
  created () {
    this.axios
      .get('http://127.0.0.1:8000/teacher/list/')
      .then((res) => {
        this.teachers = res.data
      })
      .catch((error) => {
        console.log(error)
      })
  },
  methods: {
    async deleteElem (elem) {
      await this.axios
        .delete(`http://127.0.0.1:8000/teacher/${elem}`)
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
</style>

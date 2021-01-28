<template>
  <div>
    <div><v-btn small @click='$router.go(-1)'>Back</v-btn></div>
    <v-simple-table>
      <v-data-table-header>Students</v-data-table-header>
      <tr>
        <td><strong>first_name</strong></td>
        <td><strong>last_name</strong></td>
        <td><strong>group</strong></td>
        <td></td>
        <td></td>
      </tr>
      <tr v-for="st in students" :key="st.id">
        <td>{{ st.first_name }}</td>
        <td>{{ st.last_name }}</td>
        <td>{{ st.group }}</td>
        <td><v-btn small @click='$router.push(`/student/${ st.id }`)'>Edit</v-btn></td>
        <td><v-btn small color="error" @click="deleteElem(st.id)" style="margin-right: 20px">delete</v-btn></td>
      </tr>
    </v-simple-table>
  </div>
</template>

<script>
export default {
  name: 'StudentCreate',
  data: () => ({
    students: []
  }),
  created () {
    this.axios
      .get('http://127.0.0.1:8000/student/list/')
      .then((res) => {
        this.students = res.data
      })
      .catch((error) => {
        console.log(error)
      })
  },
  methods: {
    async deleteElem (st) {
      await this.axios
        .delete(`http://127.0.0.1:8000/student/${st}`)
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

<template>
  <div class="table">
    <v-simple-table>
      <v-data-table-header>Список пар</v-data-table-header>
      <tr>
        <td><strong>День недели</strong></td>
        <td><strong>Время начала</strong></td>
        <td><strong>Группа</strong></td>
        <td><strong>Дисциплина</strong></td>
      </tr>
      <tr v-for="pair in allPairs" :key="pair.id">
        <td>{{ pair.day }}</td>
        <td>{{ pair.time }}</td>
        <td>{{ pair.group }}</td>
        <td>{{ pair.discipline }}</td>
      </tr>
    </v-simple-table>
  </div>
</template>

<script>
export default {
  name: 'Pairs',
  data: () => ({
    pairs: [],
    discipline: [],
    allPairs: []
  }),
  created () {
    this.axios
      .get('http://127.0.0.1:8000/college/pairs/')
      .then((res) => {
        this.pairs = res.data
      })
      .catch((error) => {
        console.log(error)
      })
    this.axios
      .get('http://127.0.0.1:8000/college/disciplines/')
      .then((res) => {
        this.disciplines = res.data
        for (const pair of this.pairs) {
          const p = {
            day: '',
            time: '',
            group: '',
            discipline: ''
          }
          p.day = pair.day
          p.time = pair.time
          p.group = pair.group
          const pairID = pair.discipline - 1
          p.discipline = this.disciplines[pairID].title
          this.allPairs.push(p)
        }
      })
      .catch((error) => {
        console.log(error)
      })
  }
}
</script>

<style>
.table {
  margin: 3rem;
  width: 100%;
}
</style>

<template>
  <div class="table">
    <span v-for="sch in allSchedules" :key="sch.id">
      <v-simple-table>
        <v-data-table-header>Список пар</v-data-table-header>
          <h2>{{ sch.group }}</h2>
          <tr>
            <td><strong>День недели</strong></td>
            <td><strong>Время начала</strong></td>
            <td><strong>Дисциплина</strong></td>
          </tr>
          <tr v-for="p in sch.pair" :key="p.id">
            <td>{{ p.day }}</td>
            <td>{{ p.time }}</td>
            <td>{{ p.discipline }}</td>
          </tr>
        <br>
      </v-simple-table>
    </span>
  </div>
</template>

<script>
export default {
  name: 'Schedules',
  data: () => ({
    pairs: [],
    schedules: [],
    discipline: [],
    allSchedules: []
  }),
  created () {
    this.axios
      .get('http://127.0.0.1:8000/college/schedules/')
      .then((res) => {
        this.schedules = res.data
      })
      .catch((error) => {
        console.log(error)
      })
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
        for (const schedule of this.schedules) {
          console.log(schedule)
          const s = {
            group: '',
            pair: []
          }
          s.group = schedule.group
          for (const pair of schedule.pair) {
            const p = {
              day: '0',
              time: '',
              discipline: ''
            }
            for (const curPair of this.pairs) {
              if (curPair.id === pair) {
                p.day = curPair.day
                p.time = curPair.time
                const idDisc = curPair.discipline - 1
                p.discipline = this.disciplines[idDisc].title
              }
            }
            s.pair.push(p)
            console.log(p)
          }
          this.allSchedules.push(s)
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

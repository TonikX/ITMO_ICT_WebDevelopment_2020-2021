<template>
  <div>
    <v-form
      @submit.prevent="addSchedule"
      ref="form"
      class="my-2"
    >
      <v-row>
        <v-col cols="3" class="mx-auto">
          <v-select
            label="Выберете группу для которой хотите сконфигурировать расписание"
            v-model="group"
            :items="groups">
            <option v-for="g in groups" :key="g.id">
              {{ g }}
            </option>
          </v-select>
          <v-btn @click="addSchedule">Добавить</v-btn>
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>

<script>
export default {
  name: 'ScheduleCreate',
  data: () => ({
    pairs: [],
    curPairs: [],
    groups: [],
    group: '',
    form1: {
      group: '',
      pair: ''
    },
    form2: {
      schedule: '',
      pair: ''
    },
    curSchedule: ''
  }),
  async created () {
    await this.axios
      .get('http://127.0.0.1:8000/college/pairs')
      .then((res) => {
        this.pairs = res.data
        for (const p of this.pairs) {
          if (!this.groups.includes(p.group)) {
            this.groups.push(p.group)
          }
        }
      })
      .catch((error) => {
        console.log(error)
      })
    await this.axios
      .get('http://127.0.0.1:8000/college/disciplines')
      .then((res) => {
        for (const dis of res.data) {
          for (const teacher of this.teachers) {
            if (teacher.discipline.includes(dis.id)) {
              this.disciplines.push(dis)
              break
            }
          }
        }
      })
      .catch((error) => {
        console.log(error)
      })
  },
  methods: {
    async addSchedule () {
      this.form1.group = this.group
      await this.axios
        .post('http://127.0.0.1:8000/college/schedule/create/', this.form1)
        .then((res) => {
          console.log(res)
        })
        .catch((error) => {
          console.log(error)
        })
      await this.axios
        .get('http://127.0.0.1:8000/college/schedules')
        .then((res) => {
          this.form2.schedule = res.data.length + 13
        })
        .catch((error) => {
          console.log(error)
        })
      for (const pair of this.pairs) {
        if (pair.group === this.group) {
          this.form2.pair = pair.id
          console.log(this.form2)
          await this.axios
            .post('http://127.0.0.1:8000/college/schedule/addpairs/', this.form2)
            .then((res) => {
              console.log(res)
            })
            .catch((error) => {
              console.log(error)
            })
        }
      }
      window.location.href = '/schedules'
    }
  }
}
</script>

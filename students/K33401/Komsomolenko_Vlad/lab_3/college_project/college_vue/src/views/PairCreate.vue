<template>
  <div>
    <v-form
      @submit.prevent="addPair"
      ref="form"
      class="my-2"
    >
      <v-row>
        <v-col cols="3" class="mx-auto">
          <v-select
            label="Выберете день"
            v-model="pair.day"
            :items="days">
            <option v-for="day in days" :key="day">
              {{ day }}
            </option>
          </v-select>
          <v-text-field
            label="Добавьте время"
            v-model="pair.time"
          />
          <v-text-field
            label="Добавьте группу"
            v-model="pair.group"
          />
          <v-select
            label="Выберете дисциплину"
            v-model="pair.discipline"
            :items="disciplines"
            item-text="title"
            item-value="id"
            :reduce="option => option.code">
            <option v-for="dis in disciplines" :key="dis.id">
              {{ dis.title }}
            </option>
          </v-select>
          <v-btn @click="addPair">Добавить</v-btn>
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>

<script>
export default {
  name: 'PairCreate',
  data: () => ({
    teachers: [],
    disciplines: [],
    days: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    pair: {
      day: '',
      time: '',
      group: '',
      discipline: ''
    }
  }),
  async created () {
    await this.axios
      .get('http://127.0.0.1:8000/college/teachers')
      .then((res) => {
        this.teachers = res.data
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
    async addPair () {
      console.log(this.pair)
      await this.axios
        .post('http://127.0.0.1:8000/college/pair/create/', this.pair)
        .then((res) => {
          window.location.href = '/pairs'
          console.log(res)
        })
        .catch((error) => {
          console.log(error)
        })
    }
  }
}
</script>

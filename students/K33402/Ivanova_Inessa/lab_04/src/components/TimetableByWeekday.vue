<template>
  <section>
  <table class="booking" cellpadding="10"
  v-for="elem in timetable"
  :key="elem.id">
    <tr>
      <th>{{ elem.time }}></th>
      <td>{{ elem.lesson_type.name }}</td>
      <td class>{{ elem.lesson_type.description }}</td>
      <td><button class="red-button">Записаться</button></td>
    </tr>
  </table>
  </section>
</template>

<script>
export default {
  name: 'TimetableByWeekday',
  props: {
    selectedWeekday: String
  },
  data: () => ({
    timetable: []
  }),
  methods: {
    async getTimetable (selectedWeekday) {
      // eslint-disable-next-line no-unused-vars
      let weekdayCode = ''
      const options = [
        { text: 'Понедельник', value: 'Mon' },
        { text: 'Вторник', value: 'Tue' },
        { text: 'Среда', value: 'Wen' },
        { text: 'Четверг', value: 'Thu' },
        { text: 'Пятница', value: 'Fri' },
        { text: 'Суббота', value: 'Sat' },
        { text: 'Воскресенье', value: 'Sun' }
      ]
      for (const option in options) {
        if (option.text === selectedWeekday) {
          weekdayCode = option.value
        }
      }
      try {
        const response = await this.axios
          .get('http://127.0.0.1:8000/timetable/weekdayCode')
        if (response.status !== 200) {
          throw new Error(response.error)
        }
        this.timetable = response.data
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    }
  },

  created () {
    this.getTimetable()
  }
}
</script>

<style>
  .booking {
    width: 100%;
    margin: 10px auto 20px auto;
    text-align: center;
    border-left: 2px solid red;
  }
  .red-button {
    background-color: red;
    color: white;
    padding: 10px;
    border-radius: 10px;
    border: none;
    margin-top: 10px;
    margin-bottom: 10px;
  }
</style>

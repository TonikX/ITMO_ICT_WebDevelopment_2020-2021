<template>
  <section>
  <table class="booking" cellpadding="10"
  v-for="elem in timetable"
  :key="elem.id">
    <tr>
      <th>{{ elem.time.slice(0,5) }}</th>
      <td>{{ elem.lesson_type.name }}</td>
      <td class>{{ elem.lesson_type.description }}</td>
      <td><button class="red-button" @click="addBooking(elem.id)">Записаться</button></td>
    </tr>
  </table>
  </section>
</template>

<script>
import $ from 'jquery'

export default {
  name: 'TimetableByWeekday',
  props: {
    selectedWeekday: String
  },
  data: () => ({
    timetable: []
  }),
  methods: {
    /**
     * Функция для получения расписания на день недели в переменную this.timetable
     * @param {String} selectedWeekday
     * @returns {Promise<void>}
     */
    async getTimetable (selectedWeekday) {
      try {
        const response = await this.axios
          .get(`http://127.0.0.1:8000/timetable/${selectedWeekday}`)
        if (response.status !== 200) {
          throw new Error(response.error)
        }
        this.timetable = response.data
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    /**
     * Функция для создания записи на занятие
     * @param a
     */
    addBooking (a) {
      if (sessionStorage.getItem('auth_token')) {
        $.ajax({
          url: `http://127.0.0.1:8000/book/${a}`,
          type: 'POST',
          success: (response) => {
            alert(response)
          }
        })
      } else {
        alert('Чтобы записаться, войдите в аккаунт')
        this.$router.push('login')
      }
    }
  },

  created () {
    this.getTimetable(this.selectedWeekday)
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

<template>
  <section>
    <Header />
    <NavBar />
    <div class="timetable">
      <div class="row">

        <div class="col-lg-2 align-self-end">
          <h2>Расписание</h2>
        </div>

        <div class="col-lg-2 offset-lg-8" id="weights">
          <img src="./../assets/weights.png" width="100%" alt="weights">
        </div>

      </div>
      <hr class="red-line">
      <div class="row">
        <div>
          <select v-model="selectedWeekday" class="weekday" @change="forceRerender">
            <option value="Mon">Понедельник</option>
            <option value="Tue">Вторник</option>
            <option value="Wen">Среда</option>
            <option value="Thu">Четверг</option>
            <option value="Fri">Пятница</option>
            <option value="Sat">Суббота</option>
            <option value="Sun">Воскресенье</option>
          </select>
          <timetable-by-weekday :selectedWeekday="selectedWeekday" :key="componentKey" />
        </div>
      </div>
    </div>
    <Footer />
  </section>
</template>

<script>
import Header from '@/components/Header'
import NavBar from '@/components/NavBar'
import Footer from '@/components/Footer'
import TimetableByWeekday from '@/components/TimetableByWeekday'

export default {
  name: 'Timetable',

  metaInfo: {
    title: 'Расписание',
    meta: [{
      name: 'viewport',
      content: 'width=device-width, initial-scale=1'
    }]
  },
  data: () => ({
    selectedWeekday: 'Mon',
    componentKey: 0
  }),
  components: {
    TimetableByWeekday,
    Header,
    NavBar,
    Footer
  },
  methods: {
    /**
     * Функция для обновления компоненты
     */
    forceRerender () {
      this.componentKey += 1
    }
  }
}
</script>

<style>
.timetable {
  width: 80%;
  margin-left: auto;
  margin-right: auto;
  margin-top: 10px;
  text-align: center;
}
td {
  padding: 10px 5px 10px 5px;
}
.weekday {
  padding: 7px;
  font-size: 16px;
  margin: 20px 20px 20px 15px;
  border-radius: 10px;
}
.red-line {
  background-color: red;
  height: 2px;
  margin-top: 1px;
}
</style>

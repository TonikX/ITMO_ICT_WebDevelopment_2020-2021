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
          <label>
            <select class="weekday" v-model="selectedWeekday">
              <option>Понедельник</option>
              <option>Вторник</option>
              <option>Среда</option>
              <option>Четверг</option>
              <option>Пятница</option>
              <option>Суббота</option>
              <option>Воскресенье</option>
            </select>
          </label>
          <timetable-by-weekday :selectedWeekday="selectedWeekday" />
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
  name: 'Classes',

  metaInfo: {
    title: 'Расписание',
    meta: [{
      name: 'viewport',
      content: 'width=device-width, initial-scale=1'
    }]
  },
  data: () => ({
    selectedWeekday: 'Mon'
  }),
  components: {
    TimetableByWeekday,
    Header,
    NavBar,
    Footer
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

<template>
  <section>
    <Header />
    <NavBar />
    <div class="pricelist">
      <h1>Цены на абонементы</h1>
      <div class="row1">

        <figure>
          <img src="./../assets/day.png" width="115" alt="day">
          <figcaption>
            <h4>Дневной</h4>
            <h5>8.00 - 17.00</h5>
            <h5>6500 р</h5>
          </figcaption>
        </figure>

        <figure>
          <img src="./../assets/full.png" width="115" alt="full">
          <figcaption><p>
            <h4>Полный</h4>
            <h5>8.00 - 23.00</h5>
            <h5>10 000 р</h5>
          </figcaption>
        </figure>

        <figure>
          <img src="./../assets/night.png" width="115" alt="night">
          <figcaption>
            <h4>Ночной</h4>
            <h5>17.00 - 23.00</h5>
            <h5>7000 р</h5>
          </figcaption>
        </figure>

      </div>
      <div class="row1">

        <figure>
          <img src="./../assets/clock.png" width="115" alt="clock">
          <figcaption>
            <h4>3 месяца</h4>
            <h5>36 занятий</h5>
            <h5>2500 р</h5>
          </figcaption>
        </figure>

        <figure>
          <img src="./../assets/clock.png" width="115" alt="clock">
          <figcaption>
            <h4>6 месяцев</h4>
            <h5>72 занятия</h5>
            <h5>5000 р</h5>
          </figcaption>
        </figure>

        <figure>
          <img src="./../assets/clock.png" width="115" alt="clock">
          <figcaption>
            <h4>9 месяцев</h4>
            <h5>144 занятия</h5>
            <h5>7500 р</h5>
          </figcaption>
        </figure>

      </div>
    </div>
    <div class="personal">
      <p align="center">
        <strong>Персональные занятия с тренером</strong><br>
        1 занятие - 1500 р<br>
        5 занятий - 7000 р<br>
        10 занятия - 11000 р<br>
        Месяц с тренером - 13000 р</p>
    </div>
    <div class="sale">
      <h1>Акции и скидки</h1>
      <div class="sale-row">

        <figure>
          <img class="sale-img" src="./../assets/student.jpg" alt="student">
          <figcaption>
            <h4>Скидка студентам 20% на все виды абонементов</h4>
          </figcaption>
        </figure>

        <figure>
          <img class="sale-img" src="./../assets/invite.jpg" alt="invite">
          <figcaption>
            <h4>Пригласи друга и вы оба получите скидку 15%</h4>
          </figcaption>
        </figure>
      </div>
    </div>
    <Footer />
  </section>
</template>

<script>
import Header from '@/components/Header'
import NavBar from '@/components/NavBar'
import Footer from '@/components/Footer'

export default {
  name: 'Prices',

  metaInfo: {
    title: 'Цены',
    meta: [{
      name: 'viewport',
      content: 'width=device-width, initial-scale=1'
    }]
  },
  components: {
    Header,
    NavBar,
    Footer
  }
}
</script>

<style>
  .pricelist {
    width: 60%;
    margin-left: auto;
    margin-right: auto;
    margin-top: 5px;
  }
  figure {
    text-align: center;
  }
  .row1 {
    display: flex;
    justify-content: space-between;
    width: 100%;
    margin-bottom: 1%;
  }
  .sale-row {
    display: flex;
    justify-content: space-between;
    width: 100%;
    margin-bottom: 1%;
  }
  .personal {
    display: flex;
    justify-content: center;
    font-size: 15pt;
  }
  .sale {
    width: 80%;
    margin-left: auto;
    margin-right: auto;
    margin-top: 5px;
  }
  .sale-img {
    width: 90%;
    border: 1px solid lightgray;
  }
  strong {
    font-size: 25px;
  }
  h1 {
    text-align: center;
  }
</style>

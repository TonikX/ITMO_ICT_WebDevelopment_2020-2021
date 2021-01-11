<template>
  <section>
    <Header />
    <NavBar />
    <div class="description">
      <div class="description-text">
        <h4>В здоровом теле - здоровый дух</h4>
        Фитнес клуб - это не просто возможность похудеть или набрать массу и получить красивое тело. Фитнес клуб - это путь самопознания и долго- срочного счастья. Это путь успеха и гармонии с собой и окружающим миром. Это работа над собой и эйфория от победы над своим внутренним врагом. Фитнес Клуб - это увлекательнейшее и бесконечное путешествие в себя, в мир своих безграничных возможностей!
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
  name: 'MainPage',

  metaInfo: {
    title: 'Главная',
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
.description {
  width: 100%;
  display: flex;
  height: 600px;
  background-image: url(./../assets/main.jpg);
  background-position: right;
  font-size: 13pt;
  align-items: center;
}

.description-text {
  width: 30%;
  margin-left: 8%;
  color: white;
  text-align: center;
}
</style>

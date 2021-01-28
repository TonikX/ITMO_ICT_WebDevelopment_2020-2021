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
    <div class="gallery-container">
      <h1>Наш зал</h1>
      <div class="row">
        <img src="./../assets/1.jpg" class="photo" alt="gym">
        <img src="./../assets/2.jpg" class="photo" alt="gym">
        <img src="./../assets/3.jpg" class="photo" alt="gym">
        <img src="./../assets/4.jpg" class="photo" alt="gym">
        <img src="./../assets/5.jpg" class="photo" alt="gym">
        <img src="./../assets/6.jpg" class="photo" alt="gym">
      </div>
    </div>
    <div class="address">
      <h1>Наш адрес</h1>
      <iframe class="google-map" src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d498.1747184973615!2d30.320615829273155!3d60.03664436867892!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x469634e636275c81%3A0x41009d09970baade!2z0JvQtdCz0LXQvdC00LA!5e0!3m2!1sru!2sru!4v1603482890896!5m2!1sru!2sru" width="800" height="450" frameborder="0" allowfullscreen="" aria-hidden="false" tabindex="0">
      </iframe>
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
.gallery-container {
  width: 90%;
  margin: 10px auto 0;
}
.photo {
  float: left;
  width: 33.333333%;
  padding: 10px;
  box-sizing: border-box;
}
h1 {
  text-align: center;
}
.address {
  width: 90%;
  margin: 10px auto 0;
  padding: 10px;
}
</style>

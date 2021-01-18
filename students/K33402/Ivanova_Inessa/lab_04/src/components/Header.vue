<template>
  <div class="row">
    <div class="row" id="head">
      <div class="logo col">
        <h4>Фитнес клуб</h4>
        <h6>Санкт-Петербург</h6>
      </div>
      <div class="col">
        <div class="align-self-start">
          <img src="./../assets/phone.png" width="15" height="15" alt="phone"> +7 (***) *** ** **
        </div>
        <div class="align-self-end">
          <img src="./../assets/phone.png" width="15" height="15" alt="phone"> +7 (***) *** ** **
        </div>
      </div>
      <div class="col address">
        <div class="align-self-start">
          <img src="./../assets/house.png" width="20" height="20" alt="house"> Адрес 1
        </div>
        <div class="align-self-end">
          <img src="./../assets/house.png" width="20" height="20" alt="house"> Адрес 2
        </div>
      </div>
      <div class="col">
          <button class="red-button" @click="logIn">Личный кабинет</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Header',
  methods: {
    /**
     * Функция перенаправляет пользователя в личный кабинет, если есть токен,
     * если нету, на страницу входа.
     */
    logIn () {
      if (sessionStorage.getItem('auth_token')) {
        this.$router.push('home')
      } else {
        this.$router.push('login')
      }
    }
  }
}
</script>

<style>
#head {
  display: flex;
  width: 80%;
  height: 60px;
  justify-content: space-between;
  margin: 5px auto;
  align-items: center;
  text-align: center;
}
.logo {
  text-align: center;
}
.red-button {
  background-color: red;
  color: white;
  padding: 10px 10px 10px 10px;
  border-radius: 10px;
  border: none;
}
</style>

<template>
  <section>
    <div class="row">
      <div class="row bottom">
        <div class="col-xl-3 offset-xl-1 col-lg-3 offset-lg-1 col-md-3 offset-md-1 col-sm-3 offset-sm-1 col-4">
          <div class="align-self-start">
            Наши соцсети
          </div>
          <div class="align-self-end">
            <img src="./../assets/vk.png" width="40" height="40" alt="vk">
            <img src="./../assets/inst.png" width="40" height="40" alt="inst">
            <img src="./../assets/fb.png" width="40" height="40" alt="fb">
          </div>
        </div>
        <div class="col-xl-4 col-lg-4 col-md-4 col-sm-4 col-4">
          <div class="align-self-start">
            Мобильные приложения
          </div>
          <div class="align-self-end">
            <img src="./../assets/appstore.png" height="30" alt="download_apple">
            <img src="./../assets/googleplay.png" height="30" alt="download_android">
          </div>
        </div>
        <div class="col-xl-2 offset-xl-2 col-lg-2 offset-lg-2 col-md-2 offset-md-2 col-sm-2 offset-sm-2 col-3 offset-1">
          Copyright 2020
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'Footer'
}
</script>

<style>
.bottom {
  width: 100%;
  height: 80px;
  padding: 5px 5px 5px 5px;
  background-color: black;
  color: white;
  margin-right: 0;
  margin-left: 0;
}
img {
  padding: 3px
}
</style>

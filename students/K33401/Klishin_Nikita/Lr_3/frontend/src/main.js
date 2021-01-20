import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify';
import store from './store'

Vue.config.productionTip = false

new Vue({
  store: store,
  router,
  vuetify,
  render: function (h) { return h(App) }
}).$mount('#app')

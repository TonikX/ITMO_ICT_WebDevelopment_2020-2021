import Vue from 'vue'
import VueRouter from 'vue-router'
import Greeting from '../components/Greeting'
import Nasa from '../components/Nasa'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Greeting',
    component: Greeting
  },

  {
    path: '/nasa',
    name: 'Nasa',
    component: Nasa
  }

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

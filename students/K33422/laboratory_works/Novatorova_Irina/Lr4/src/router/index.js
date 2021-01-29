import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import SignUp from '../views/SignUp.vue'
import Application from '../views/Application.vue'
import Client from '../views/Client.vue'
import Materials from '../views/Materials.vue'
import Services from '../views/Services.vue'
import Worker from '../views/Worker.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/application',
    name: 'Application',
    component: Application
  },
  {
    path: '/client',
    name: 'Client',
    component: Client
  },
  {
    path: '/materials',
    name: 'Materials',
    component: Materials
  },
  {
    path: '/services',
    name: 'Services',
    component: Services
  },
  {
    path: '/worker',
    name: 'Worker',
    component: Worker
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

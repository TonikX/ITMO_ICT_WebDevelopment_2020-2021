import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'
import Login from '@/components/Login.vue'
import OneBook from '@/components/OneBook.vue'
import Books from '@/components/Books'
import ChooseInterface from '@/components/ChooseInterface'
import Readers from '@/components/Readers'
import OneReader from '@/components/OneReader'
import InstancesOfBook from '@/components/InstancesOfBook'
import OneInstanceOfBook from '@/components/OneInstanceOfBook'
import IssuingAInstances from '@/components/IssuingAInstances'
import OneIssuingAInstances from '@/components/OneIssuingAInstances'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/oneBook',
    name: 'OneBook',
    component: OneBook
  },
  {
    path: '/books',
    name: 'Books',
    component: Books
  },
  {
    path: '/chooseInterface',
    name: 'ChooseInterface',
    component: ChooseInterface
  },
  {
    path: '/readers',
    name: 'Readers',
    component: Readers
  },
  {
    path: '/oneReader',
    name: 'OneReader',
    component: OneReader
  },
  {
    path: '/instancesOfBook',
    name: 'InstancesOfBook',
    component: InstancesOfBook
  },
  {
    path: '/oneInstanceOfBook',
    name: 'OneInstanceOfBook',
    component: OneInstanceOfBook
  },
  {
    path: '/issuingAInstances',
    name: 'IssuingAInstances',
    component: IssuingAInstances
  },
  {
    path: '/oneIssuingAInstances',
    name: 'OneIssuingAInstances',
    component: OneIssuingAInstances
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

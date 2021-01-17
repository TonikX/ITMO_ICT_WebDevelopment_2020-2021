import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'
import Login from '@/components/Login.vue'
import CreateBook from '@/components/CreateBook.vue'
import OneBook from '@/components/OneBook.vue'
import Books from '@/components/Books'
import ChooseInterface from '@/components/ChooseInterface'
import Readers from '@/components/Readers'
import OneReader from '@/components/OneReader'

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
    path: '/createBook',
    name: 'CreateBook',
    component: CreateBook
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
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

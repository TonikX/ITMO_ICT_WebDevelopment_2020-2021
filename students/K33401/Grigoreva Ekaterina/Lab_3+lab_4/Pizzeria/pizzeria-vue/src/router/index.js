import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'
import SignIn from '@/views/SignIn'
import SignUp from '@/views/SignUp'
import Pizza from '@/views/Pizza'
import PersonalPage from '@/views/PersonalPage'
import Orders from '@/views/Orders'
import SignOut from '@/views/SignOut'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/signin',
    name: 'SignIn',
    component: SignIn
  },
  {
    path: '/signout',
    name: 'SignOut',
    component: SignOut
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/pizza',
    name: 'Pizza',
    component: Pizza
  },
  {
    path: '/orders',
    name: 'Orders',
    component: Orders
  },
  {
    path: '/personalpage',
    name: 'PersonalPage',
    component: PersonalPage
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

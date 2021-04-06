import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'
import Login from '@/views/Login'
import PersonalPage from '@/views/PersonalPage'
import Logout from '@/views/Logout'
import Registration from '@/views/Registration'
import Cabinet from '@/views/Cabinet'
import Patient from '@/views/Patient'
import Price from '@/views/Price'
import Diagnosis from '@/views/Diagnosis'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/logout',
    name: 'Logout',
    component: Logout
  },
  {
    path: '/register',
    name: 'Register',
    component: Registration
  },
  {
    path: '/personalpage',
    name: 'PersonalPage',
    component: PersonalPage
  },
  {
    path: '/patient',
    name: 'Patient',
    component: Patient
  },
  {
    path: '/cabinet',
    name: 'Cabinet',
    component: Cabinet
  },
  {
    path: '/diagnosis',
    name: 'Diagnosis',
    component: Diagnosis
  },
  {
    path: '/price',
    name: 'Price',
    component: Price
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

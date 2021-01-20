import Vue from 'vue'
import VueRouter from 'vue-router'
import MainPage from '../views/MainPage'
import Auth from '../views/Auth'
import SignUp from '../views/SignUp'
import SignOut from '../views/SignOut'
import MyAnimals from '../views/MyAnimals'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'MainPage',
    component: MainPage
  },
  {
    path: '/signin',
    name: 'SignIn',
    component: Auth
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/signout',
    name: 'SignOut',
    component: SignOut
  },
  {
    path: '/animals',
    name: 'MyAnimals',
    component: MyAnimals
  }

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

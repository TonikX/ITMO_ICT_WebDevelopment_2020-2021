import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import SignUp from '../views/SignUp.vue'
import SignIn from '../views/SignIn.vue'
import UserInfo from '../views/Settings.vue'
import ChickensList from '../views/Chickens.vue'
import BreedsList from '../views/Breeds.vue'
import CellsList from '../views/Cells.vue'

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
    path: '/signin',
    name: 'SignIn',
    component: SignIn
  },
  {
    path: '/settings',
    name: 'UserInfo',
    component: UserInfo
  },
  {
    path: '/chickenslist',
    name: 'ChickensList',
    component: ChickensList
  },
  {
    path: '/breedslist',
    name: 'BreedsList',
    component: BreedsList
  },
  {
    path: '/cellslist',
    name: 'CellsList',
    component: CellsList
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

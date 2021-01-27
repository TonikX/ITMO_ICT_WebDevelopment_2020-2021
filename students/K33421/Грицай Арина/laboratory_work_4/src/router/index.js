import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import SignUp from '@/views/SignUp.vue'
import UserInfo from '@/views/Profile.vue'
import ChickensList from '@/views/Chickens.vue'
import BreedsList from '@/views/Breeds.vue'
import CellsList from '@/views/Cells.vue'

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
    path: '/profile',
    name: 'Profile',
    component: Profile
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
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

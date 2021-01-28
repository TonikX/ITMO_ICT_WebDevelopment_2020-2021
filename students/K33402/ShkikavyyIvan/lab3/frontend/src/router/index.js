import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'
import Login from '@/components/Login.vue'
import Creation from '@/components/Creation'
import Author from '@/components/Author'
import Review from '@/components/Review'
import Signin from '@/components/Signin'
import LK from '@/components/LK'
import Editlc from '@/components/Editlc'
import Authorlist from '@/components/Authorlist'
import NewCreation from '@/components/NewCreation'
import NewAuthor from '@/components/NewAuthor'
import Start from '@/components/Start'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Start',
    component: Start
  },
  {
    path: '/home',
    name: 'Home',
    component: Home
  },
  {
    path: '/new_creation',
    name: 'NewCreation',
    component: NewCreation
  },
  {
    path: '/new_author',
    name: 'NewAuthor',
    component: NewAuthor
  },
  {
    path: '/lc/edit',
    name: 'Editlc',
    component: Editlc
  },
  {
    path: '/lc',
    name: 'LK',
    component: LK
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/signin',
    name: 'Signin',
    component: Signin
  },
  {
    path: '/creation/:id',
    name: 'Creation',
    component: Creation
  },
  {
    path: '/author/:id',
    name: 'Author',
    component: Author
  },
  {
    path: '/review',
    name: 'Review',
    component: Review
  },
  {
    path: '/authorlist',
    name: 'Authorlist',
    component: Authorlist
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

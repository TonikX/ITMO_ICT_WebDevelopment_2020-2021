import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import CreateClimber from '../components/CreateClimber.vue'
import CreatePeak from '../components/CreatePeak.vue'
import ClimberList from '../components/ClimberList.vue'
import PeakList from '../components/PeakList.vue'
import Peak from '../views/Peak.vue'
import UpdatePeak from '../components/UpdatePeak.vue'
import ClimbingList from '../components/ClimbingList.vue'
import CreateClimbing from '../components/CreateClimbing.vue'
import CreateParticipation from '../components/CreateParticipation.vue'
import CreateEmergency from '../components/CreateEmergency.vue'
import Account from '../views/Account.vue'
import Register from '../components/Register.vue'
import Login from '../components/Login.vue'
import UpdateAccount from '../components/UpdateAccount.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/climbers/create',
    name: 'CreateClimber',
    component: CreateClimber
  },
  {
    path: '/peaks/create',
    name: 'CreatePeak',
    component: CreatePeak
  },
  {
    path: '/climbers/',
    name: 'ClimberList',
    component: ClimberList
  },
  {
    path: '/peaks',
    component: Peak,
    children: [
      {
        path: 'no_climbings',
        component: PeakList,
      },
      {
        path: ':pk',
        component: UpdatePeak,
      },
      {
        path: '',
        component: PeakList,
      },
    ]
  },
  {
    path: '/climbings/create',
    component: CreateClimbing
  },
  {
    path: '/climbings',
    component: ClimbingList,
  },
  {
    path: '/participations/create',
    component: CreateParticipation,
  },
  {
    path: '/emergencies/create',
    component: CreateEmergency,
  },
  {
    path: '/account',
    component: Account,
    children: [
      {
        path: 'register',
        component: Register,
      },
       {
         path: 'login',
         component: Login,
       },
       {
         path: '',
         component: UpdateAccount,
       }
    ]
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: function () {
      return import(/* webpackChunkName: "about" */ '../views/About.vue')
    }
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home'
import Login from '../views/Login'
import Register from '../views/Register'
import Room from '../views/Room'
import RoomCreate from '../views/RoomCreate'
import RoomDetail from '../views/RoomDetail'
import Staff from '../views/Staff'
import StaffCreate from '../views/StaffCreate'
import StaffDetail from '../views/StaffDetail'
import GuestDetail from '../views/GuestDetail'
import GuestCreate from '../views/GuestCreate'
import Profile from '../views/Profile'

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
    path: '/register',
    name: 'Register',
    component: Register
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile
  },
  {
    path: '/room',
    name: 'Room',
    component: Room
  },
  {
    path: '/room/create',
    name: 'RoomCreate',
    component: RoomCreate
  },
  {
    path: '/room/:room_id',
    name: 'RoomDetail',
    component: RoomDetail
  },
  {
    path: '/staff',
    name: 'Staff',
    component: Staff
  },
  {
    path: '/staff/create',
    name: 'StaffCreate',
    component: StaffCreate
  },
  {
    path: '/staff/:staff_id',
    name: 'StaffDetail',
    component: StaffDetail
  },
  {
    path: '/guest/create',
    name: 'GuestCreate',
    component: GuestCreate
  },
  {
    path: '/guest/:guest_id',
    name: 'GuestDetail',
    component: GuestDetail
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

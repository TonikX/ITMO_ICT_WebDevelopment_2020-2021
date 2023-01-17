import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import SignUp from '@/views/SignUp'
import SignIn from '@/views/SignIn'
import Profile from '@/views/Profile'
import EditProfile from '@/views/EditProfile'
import Rooms from '@/views/Rooms'
import Subjects from '@/views/Subjects'
import Teachers from '@/views/Teachers'
import Students from '@/views/Students'
import Groups from '@/views/Groups'
import Teachings from '@/views/Teachings'
import Schedule from '@/views/Schedule'
import MySchedule from '@/views/MySchedule'
import Grades from '@/views/Grades'
import MyGrades from '@/views/MyGrades'
import Account from '@/views/TeacherStudentProfile'

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
    path: '/profile/edit',
    name: 'EditProfile',
    component: EditProfile
  },
  {
    path: '/rooms',
    name: 'Rooms',
    component: Rooms
  },
  {
    path: '/subjects',
    name: 'Subjects',
    component: Subjects
  },
  {
    path: '/teachers',
    name: 'Teachers',
    component: Teachers
  },
  {
    path: '/groups',
    name: 'Groups',
    component: Groups
  },
  {
    path: '/students',
    name: 'Students',
    component: Students
  },
  {
    path: '/teachings',
    name: 'Teachings',
    component: Teachings
  },
  {
    path: '/schedule',
    name: 'Schedule',
    component: Schedule
  },
  {
    path: '/myschedule',
    name: 'MySchedule',
    component: MySchedule
  },
  {
    path: '/grades',
    name: 'Grades',
    component: Grades
  },
  {
    path: '/mygrades',
    name: 'MyGrades',
    component: MyGrades
  },
  {
    path: '/account',
    name: 'Account',
    component: Account
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

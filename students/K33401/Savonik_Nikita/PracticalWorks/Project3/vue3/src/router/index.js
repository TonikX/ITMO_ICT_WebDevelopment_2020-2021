import Vue from 'vue'
import VueRouter from 'vue-router'
import SignUp from '../views/SignUp'
import SignIn from '../views/SignIn'
import HomeDeputy from '../views/HomeDeputy'
import HomeManager from '../views/HomeManager'
import Mark from '../views/Mark'
import MarkCreate from '../views/MarkCreate'
import MarkEdit from '../views/MarkEdit'
import Teacher from '../views/Teacher'
import TeacherNew from '../views/TeacherNew'
import TeacherEdit from '../views/TeacherEdit'
import Student from '../views/Student'
import StudentCreate from '../views/StudentCreate'
import StudentEdit from '../views/StudentEdit'
import Pair from '../views/Pair'
import PairCreate from '../views/PairCreate'
import PairEdit from '../views/PairEdit'
import Subject from '../views/Subject'
import SubjectCreate from '../views/SubjectCreate'
import SubjectEdit from '../views/SubjectEdit'
import Home from '../views/Home'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/deputy',
    name: 'HomeDeputy',
    component: HomeDeputy
  },
  {
    path: '/manager',
    name: 'HomeManager',
    component: HomeManager
  },
  {
    path: '/student',
    name: 'Student',
    component: Student
  },
  {
    path: '/student/create',
    name: 'StudentCreate',
    component: StudentCreate
  },
  {
    path: '/student/:student_id',
    name: 'StudentEdit',
    component: StudentEdit
  },
  {
    path: '/mark',
    name: 'Mark',
    component: Mark
  },
  {
    path: '/mark/create',
    name: 'MarkCreate',
    component: MarkCreate
  },
  {
    path: '/mark/:mark_id',
    name: 'MarkEdit',
    component: MarkEdit
  },
  {
    path: '/subject',
    name: 'Subject',
    component: Subject
  },
  {
    path: '/subject/create',
    name: 'SubjectCreate',
    component: SubjectCreate
  },
  {
    path: '/subject/:subject_id',
    name: 'SubjectEdit',
    component: SubjectEdit
  },
  {
    path: '/pair',
    name: 'Pair',
    component: Pair
  },
  {
    path: '/pair/create',
    name: 'PairCreate',
    component: PairCreate
  },
  {
    path: '/pair/:pair_id',
    name: 'PairEdit',
    component: PairEdit
  },
  {
    path: '/teacher',
    name: 'Teacher',
    component: Teacher
  },
  {
    path: '/teacher/create',
    name: 'TeacherNew',
    component: TeacherNew
  },
  {
    path: '/teacher/:teacher_id',
    name: 'TeacherEdit',
    component: TeacherEdit
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
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

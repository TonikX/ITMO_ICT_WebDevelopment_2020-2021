import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import UserCreate from '../views/UserCreate.vue'
import Student from '../views/Student.vue'
import UpdateStudent from '../views/UpdateStudent.vue'
import CreateStudent from '../views/StudentCreate.vue'
import Teacher from '../views/Teacher.vue'
import UpdateTeacher from '../views/UpdateTeacher.vue'
import CreateTeacher from '../views/TeacherCreate.vue'
import DisciplineCreate from '../views/DisciplineCreate.vue'
import Mark from '../views/Mark.vue'
import MarkCreate from '../views/MarkCreate.vue'
import UpdateMark from '../views/UpdateMark.vue'
import Subjects from '../views/Subjects.vue'
import Pairs from '../views/Pairs.vue'
import Schedules from '../views/Schedules.vue'
import PairCreate from '../views/PairCreate.vue'
import ScheduleCreate from '../views/ScheduleCreate.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/createuser',
    name: 'UserCreate',
    component: UserCreate
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/students',
    name: 'Student',
    component: Student
  },
  {
    path: '/createstudent',
    name: 'CreateStudent',
    component: CreateStudent
  },
  {
    path: '/updatestudent/:student_id',
    name: 'UpdateStudent',
    component: UpdateStudent
  },
  {
    path: '/teachers',
    name: 'Teacher',
    component: Teacher
  },
  {
    path: '/createteacher',
    name: 'CreateTeacher',
    component: CreateTeacher
  },
  {
    path: '/updateteacher/:teacher_id',
    name: 'UpdateTeacher',
    component: UpdateTeacher
  },
  {
    path: '/creatediscipline',
    name: 'DisciplineCreate',
    component: DisciplineCreate
  },
  {
    path: '/marks',
    name: 'Mark',
    component: Mark
  },
  {
    path: '/markcreate',
    name: 'MarkCreate',
    component: MarkCreate
  },
  {
    path: '/updatemark/:mark_id',
    name: 'UpdateMark',
    component: UpdateMark
  },
  {
    path: '/subjects',
    name: 'Subjects',
    component: Subjects
  },
  {
    path: '/pairs',
    name: 'Pairs',
    component: Pairs
  },
  {
    path: '/schedules',
    name: 'Schedules',
    component: Schedules
  },
  {
    path: '/paircreate',
    name: 'PairCreate',
    component: PairCreate
  },
  {
    path: '/schedulecreate',
    name: 'ScheduleCreate',
    component: ScheduleCreate
  }
]
const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

import Vue from 'vue'
import VueRouter from 'vue-router'

import MainPage from "@/views/MainPage"
import Register from "@/views/auth/Register"
import Login from "@/views/auth/Login"
import Logout from "@/views/auth/Logout"
import Profile from "@/views/auth/Profile"
import Task from "@/views/Task"
import AddTask from "@/views/AddTask"
import GroupsList from "@/views/GroupsList"
import Criterions from "@/views/CriterionsList"
import NotFound from "@/components/NotFound"

Vue.use(VueRouter)

const routes = [
  {
    path: "/",
    name: "main",
    component: MainPage
  },
  {
    path: "/login",
    name: "login",
    component: Login
  },
  {
    path: "/logout",
    name: "logout",
    component: Logout
  },
  {
    path: "/register",
    name: "registration",
    component: Register
  },
  {
    path: "/profile",
    name: "profile",
    component: Profile
  },
  {
    path: "/tasks",
    // alias: "/tasks",
    name: "tasks",
    component: () => import("../views/TasksList")
  },
  {
    path: "/task/:id",
    name: "task",
    component: Task,
    props: true,
  },
  {
    path: "/add",
    name: "add_task",
    component: AddTask,
  },
  {
    path: "/classes",
    name: "student_classes",
    component: GroupsList,
  },
  {
    path: "/criterions",
    name: "criterions",
    component: Criterions,
  },
  {
    path: "*",
    name: "not found",
    component: NotFound
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

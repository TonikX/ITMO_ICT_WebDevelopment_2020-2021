import VueRouter from 'vue-router';

import Hello from "../views/Hello";
import Account from "../views/Account";
import Register from "../views/Register";
import Login from "../views/Login";
import Wishlist from "../views/Wishlist";

export default new VueRouter({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Hello',
      component: Hello
    },
    {
      path: '/account',
      name: 'Account',
      component: Account
    },
    {
      path: '/register',
      name: 'Register',
      component: Register
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/wishlist/:userId',
      name: 'Wishlist',
      component: Wishlist
    }
  ]
})
<template>
    <v-app-bar color="#005B7C" dark elevation="3" app>
      <v-toolbar-items id="Logo">
        <v-btn color="#005B7C" elevation="0" v-on:click="$router.push('/')">
           <v-toolbar-title v-text="'Fluffy Friend'"/>
        </v-btn>
      </v-toolbar-items>

      <v-spacer />
      <v-toolbar-items v-if="loggedIn" id="navi">
        <v-btn color="#005B7C" elevation="0" :to="'/animals'" >
          <v-icon left v-html="catLogo"> </v-icon>
          Мои животные
        </v-btn>
          <menu-component />
      </v-toolbar-items >
      <v-toolbar-items v-else id="navi">
        <v-btn v-for="(item, i) in menuItemsNotLogged" color="#005B7C" elevation="0" :key="`menuItems${i}`" :to="item.route" >
          <v-icon left v-html="item.icon"> </v-icon>
          {{item.title}}
        </v-btn>
      </v-toolbar-items>
    </v-app-bar>
</template>

<script>
import {
  mdiLoginVariant,
  mdiLockOpenOutline,
  mdiCat
} from '@mdi/js'
import MenuComponent from './Menu'

export default {

  name: 'HeaderComponent',
  components: { MenuComponent },
  props: {
    loggedIn: Boolean,
    username: String
  },
  data: () => ({
    catLogo: mdiCat
  }),
  computed: {
    /**
     * Выводит спиисок элементов меню если пользователь не залогинен
     * @returns {({route: string, icon: string, title: string}|{route: string, icon: string, title: string})[]}
     */
    menuItemsNotLogged () {
      return [
        {
          icon: mdiLoginVariant,
          title: 'Войти',
          route: '/signin'
        },
        {
          icon: mdiLockOpenOutline,
          title: 'Зарегистрироваться',
          route: '/signup'
        }
      ]
    }
  }
}
</script>

<style scoped>
  #navi {
    margin-right: 15%;
  }

  #Logo {
    margin-left: 15%;
  }
</style>

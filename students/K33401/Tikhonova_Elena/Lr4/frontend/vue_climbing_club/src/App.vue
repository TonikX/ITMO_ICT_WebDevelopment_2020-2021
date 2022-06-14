  
<template>
  <v-app id="inspire">
    <v-navigation-drawer dark color="mycolor" v-model="drawer" app>
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="title">
            This is a frontend
          </v-list-item-title>
          <v-list-item-subtitle>
            part of climbing club project
          </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>

      <v-list dense nav>
        <v-list-item v-for="item in items" :key="item.title" :to="item.to" link>
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar
      app
      dark
      absolute
      color="secondary"
      shrink-on-scroll
      prominent
      src="https://www.powrock.com/MTF//Content/Catalog/location_activity/italy/PRODUCTS/arrampicata-cover-01__4564181389021871108.jpg"
      fade-img-on-scroll
      scroll-target="#scrolling-techniques-2"
      scroll-threshold="300"
    >
      <template v-slot:img="{ props }">
        <v-img
          v-bind="props"
          gradient="to top right, rgba(30,30,45,.9), rgba(200,150,160,.2)"
        ></v-img>
      </template>

      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

      <v-toolbar-title>Climbing club!</v-toolbar-title>
    </v-app-bar>
    <v-sheet
      id="scrolling-techniques-2"
      class="overflow-y-auto"
      max-height="1009"
    >
      <v-container>
        <v-main>
          <router-view>
            <!-- <v-container style="height: 1080px"></v-container> -->
          </router-view>
        </v-main>
      </v-container>
    </v-sheet>

    <v-footer absolute color="mycolor" dark>
      <v-col class="text-right" cols="12">
        {{ new Date().getFullYear() }} —
        <strong>SuperProjectClimbingClub</strong>
      </v-col>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  data: () => ({
    drawer: null,
    items: [
      { title: "Home", icon: "mdi-home", to: "/" },
      { title: "About", icon: "mdi-help-circle", to: "/about" },
      { title: "My account", icon: "mdi-account-cowboy-hat", to: "/account" },
    ],
  }),
};
</script>
<style>
.mb-footer {
  margin-bottom: 90px;
}
/* ::-webkit-scrollbar { 
    display: none; 
} */
</style>

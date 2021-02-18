<template>
    <v-container>
    <v-row>
      <v-col >
         <v-card
           dark
          absolute
          permanent
  >
    <v-list  >
      <v-subheader>DISPATCHER'S SITE NAVIGATION</v-subheader>
      <v-list-item-group
        v-model="selectedItem"
        color="primary">

        <v-list-item href="/profile">
          <v-list-item-icon>
            <v-icon>mdi-account</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            My profile
          </v-list-item-content>
        </v-list-item>

        <v-list-item href="/schedule">
          <v-list-item-icon>
            <v-icon>mdi-calendar</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            Schedule management
          </v-list-item-content>
        </v-list-item>

        <v-list-item href="/teachers">
          <v-list-item-icon>
            <v-icon>mdi-account-tie</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            Teachers' accounts
          </v-list-item-content>
        </v-list-item>

        <v-list-item href="/students">
          <v-list-item-icon>
            <v-icon>mdi-account-tie-outline</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            Students' accounts
          </v-list-item-content>
        </v-list-item>

        <v-list-item href="/groups">
          <v-list-item-icon>
            <v-icon>mdi-account-group</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            Groups management
          </v-list-item-content>
        </v-list-item>

        <v-list-item href="/rooms">
          <v-list-item-icon>
            <v-icon>mdi-google-classroom</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            Rooms management
          </v-list-item-content>
        </v-list-item>

      </v-list-item-group>
    </v-list>
  </v-card>
      </v-col>
    </v-row>
  </v-container>

</template>

<script>
export default {
  name: 'NavMenuDis',
  props: {
    role: String
  }
}
</script>

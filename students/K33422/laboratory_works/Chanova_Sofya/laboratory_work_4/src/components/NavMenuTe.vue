<template>
    <v-container>
    <v-row>
      <v-col cols="4">
         <v-card
           dark
          absolute
          permanent
  >
    <v-list  >
      <v-subheader> TEACHER'S SITE NAVIGATION</v-subheader>
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

        <v-list-item href="/">
          <v-list-item-icon>
            <v-icon>mdi-account</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            Schedule
          </v-list-item-content>
        </v-list-item>

        <v-list-item href="/">
          <v-list-item-icon>
            <v-icon>mdi-account</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            My schedule
          </v-list-item-content>
        </v-list-item>

        <v-list-item href="/">
          <v-list-item-icon>
            <v-icon>mdi-account</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            My teachings
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
  name: 'NavMenuTe',
  props: {
    role: String
  }
}
</script>

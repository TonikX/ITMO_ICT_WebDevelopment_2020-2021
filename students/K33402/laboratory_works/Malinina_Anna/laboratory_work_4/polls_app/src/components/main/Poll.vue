<template>
  <v-card
    elevation="2"
    class="px-2 py-5"
  >
    <v-row>
      <v-col cols="3">
        <v-card-text>
          <router-link :to="{ name: 'Details', params: { pollId: poll.id }}">{{poll.title}}</router-link>
        </v-card-text>
      </v-col>

      <v-col cols="3">
        <v-card-text>
          {{ poll.theme }}
        </v-card-text>
      </v-col>
      <v-col cols="2">
        <v-card-text>
          {{ poll.creator }}
        </v-card-text>
      </v-col>
      <v-col cols="2">
        <v-card-text>
          {{ poll.create_date }}
        </v-card-text>
      </v-col>
      <v-col cols="2">
        <v-card-text>
          {{ poll.voting_time }} минут
        </v-card-text>
      </v-col>
    </v-row>
  </v-card>
</template>

<script>
export default {
  name: 'Poll',

  props: {
    poll: Object
  }
}
</script>

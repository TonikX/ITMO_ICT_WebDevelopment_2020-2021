<template>
<v-container>
  <v-row>
      <template v-for="(climber, n) in climbers">
        <v-col :key="n">
          <v-card class="pa-2 mb-5" height="170">
        <v-card-title>{{climber.first_name+" "+climber.last_name}}</v-card-title>
        <v-card-subtitle>A member of club "{{clubs[climber.club]}}"</v-card-subtitle>
        <v-card-text>
          Address: {{climber.address}}
        </v-card-text>
      </v-card>
        </v-col>
        <v-responsive
          v-if="(n+1)%2 === 0"
          :key="`width-${n}`"
          width="100%"
        ></v-responsive>
      </template>
    </v-row>
</v-container>
</template>
<script>
export default {
    name: 'ClimberList',
    data: () => ({
      climbers: Object,
      clubs: Object,
    }),
    mounted () {
      this.getContext()
    },
    methods: {
      getContext() {
        this.axios.get('//127.0.0.1:9000/climbers/').then((response) => {
          console.log(response.data)
          this.climbers = response.data});
        this.axios.get('//127.0.0.1:9000/clubs/').then((response) => {
          console.log(response.data)
          response.data.forEach(obj => {
            this.clubs[obj.id] = obj.name
          })
          // this.clubs = response.data
          });
          console.log(this.climbers)
          console.log(this.clubs)
      }
    }
}
</script>

<template>
  <v-container>
    <v-row>
      <template v-for="(peak, n) in peaks">
        <v-col :key="n">
          <v-card class="pa-2 mb-5" min-height="170">
            <v-card-title>{{
              peak.name + " - " + peak.height + " м."
            }}</v-card-title>
            <v-card-subtitle>{{ peak.country }}</v-card-subtitle>
            <v-card-actions>
              <v-btn @click="show = true" color="orange lighten-2" text>
                Explore
              </v-btn>

              <v-spacer></v-spacer>

              <v-btn icon @click="show = !show">
                <v-icon>{{
                  show ? "mdi-chevron-up" : "mdi-chevron-down"
                }}</v-icon>
              </v-btn>
            </v-card-actions>
            <v-expand-transition>
              <div v-show="show">
                <v-divider></v-divider>

                <!-- <v-card-text v-html="peak.route_description.split('.').join('.</br>')"> -->
                <v-card-text>
                  {{ peak.route_description }}
                </v-card-text>
              </div>
            </v-expand-transition>
          </v-card>
        </v-col>
        <v-responsive
          v-if="(n + 1) % 2 === 0"
          :key="`width-${n}`"
          width="100%"
        ></v-responsive>
      </template> </v-row
    ><v-row justify="space-around">
      <v-btn :to="getBtnLink" class="mb-footer" outlined large>{{
        getBtnName
      }}</v-btn></v-row
    >
  </v-container>
</template>
<script>
import UpdatePeak from "./UpdatePeak.vue";
export default {
  components: { UpdatePeak },
  name: "PeakList",
  data: () => ({
    show: false,
    peaks: [],
  }),
  computed: {
    getBtnName: function () {
      if (this.$route.path.includes("no_climbings")) {
        return "View full list";
      }
      return "View list without climbings";
    },
    getBtnLink: function () {
      if (this.$route.path.includes("no_climbings")) {
        return "/peaks/";
      }
      return "/peaks/no_climbings";
    },
  },
  mounted() {
    this.getContext();
    console.log(this.$route);
  },
  updated() {
    this.getContext();
  },
  methods: {
    getContext() {
      this.axios.get("//127.0.0.1:9000" + this.$route.path).then((response) => {
        console.log(response.data);
        this.peaks = response.data;
      });
      console.log(this.peaks);
    },
  },
};
</script>

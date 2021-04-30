<template>
  <v-card>
    <v-card-title>Climbing list</v-card-title>
    <v-data-table
      hide-default-footer
      :headers="headers"
      :items="climbings"
      :sort-by="['peak']"
    ></v-data-table
    ><v-container>
      <v-form>
        <v-row justify="space-around">
          <v-col cols="4">
            <v-date-picker
              color="mycolor"
              v-model="picker1"
            ></v-date-picker></v-col
          ><v-col cols="4">
            <v-date-picker
              color="mycolor"
              v-model="picker2"
            ></v-date-picker></v-col
        ></v-row>
        <v-row justify="space-around" class="pb-5">
          <v-btn
            outlined
            large
            :to="'?from=' + picker1 + '&to=' + picker2"
            @click="getClimbings()"
            >View results!</v-btn
          ></v-row
        >
      </v-form></v-container
    >
  </v-card>
</template>

<script>
// ?from=2021-04-07&to=2021-04-11
export default {
  data: () => ({
    picker1: new Date().toISOString().substr(0, 10),
    picker2: new Date().toISOString().substr(0, 10),
    peaks: Object,
    climbings: [],
    headers: [
      {
        text: "Peak name",
        value: "peak",
      },
      { text: "Start", value: "start_time" },
      { text: "Finish", value: "finish_time" },
      { text: "Information", value: "information" },
    ],
  }),
  mounted() {
    this.getPeaks();
    this.getClimbings();
  },
  // updated() {
  //   this.getClimbings();
  // },
  methods: {
    getPeaks() {
      console.log(this.$route.path);

      this.axios.get("//127.0.0.1:9000/peaks/").then((response) => {
        //console.log(response.data);
        response.data.forEach((element) => {
          this.peaks[element.id] =
            element.name + " (" + element.height + " м.)";
        });
      });
    },
    getClimbings() {
      this.axios
        .get("//127.0.0.1:9000" + this.$route.fullPath)
        .then((response) => {
          console.log("route is ", this.$route.fullPath);
          console.log(response.data);
          this.climbings = response.data;
          this.climbings.forEach((element) => {
            element.peak = this.peaks[element.peak];
            element.start_time = element.start_time
              .replace(/T.*Z/, "")
              .split("-")
              .reverse()
              .join(".");
            if (element.finish_time !== null) {
              element.finish_time = element.finish_time
                .replace(/T.*Z/, "")
                .split("-")
                .reverse()
                .join(".");
            }
          });
          console.log("hello");
          console.log(this.climbings);
        });
      // this.peaks = response.data;
    },
  },
};
</script>

<template>
  <v-form class="mb-footer">
    <v-container>
      <v-card class="my-5">
        <v-card-title>Create a climbing</v-card-title>
        <v-row justify="space-around"
          ><v-col cols="10">
            <v-select
              v-model="selected_peak"
              :items="peaks"
              item-value="id"
              item-text="name"
              label="Peak"
              outlined
              return-object
              @change="someF()"
            ></v-select
          ></v-col>
        </v-row>
        <v-row justify="space-around">
          <v-col cols="4">
            <v-time-picker
              use-seconds
              v-model="fromtime"
              format="24hr"
            ></v-time-picker>
          </v-col>
          <v-col cols="4">
            <v-date-picker v-model="fromdate"></v-date-picker> </v-col
        ></v-row>
        <v-row justify="space-around">
          <v-col cols="4">
            <v-time-picker
              use-seconds
              v-model="totime"
              format="24hr"
            ></v-time-picker>
          </v-col>
          <v-col cols="4">
            <v-date-picker v-model="todate"></v-date-picker> </v-col
        ></v-row>
        <v-row justify="space-around">
          <v-col cols="10">
            <v-textarea
              v-model="climbing.information"
              clearable
              clear-icon="mdi-close-circle"
              label="Information"
              placeholder="Все прошло просто замечательно!"
            ></v-textarea>
          </v-col>
        </v-row>
        <v-row justify="space-around" class="pb-5">
          <v-btn outlined large class="text-center" @click="postObj">
            Создать!
          </v-btn></v-row
        >
      </v-card>
    </v-container>
  </v-form>
</template>
<script>
export default {
  name: "CreateClimbing",
  data: () => ({
    selected_peak: null,
    peaks: Object,
    fromtime: "",
    fromdate: "",
    totime: "",
    todate: "",
    climbing: {
      peak: null,
      start_time: "",
      finish_time: "",
      participants: null,
      information: "",
    },
    reqRules: [(v) => !!v || "This field is required"],
  }),
  mounted() {
    this.getPeaks();
  },
  methods: {
    getPeaks() {
      this.axios.get("//127.0.0.1:9000/peaks/").then((response) => {
        this.peaks = response.data;
      });
    },
    postObj() {
      this.climbing.peak = this.selected_peak.id;
      this.climbing.start_time = this.fromdate + "T" + this.fromtime + "Z";
      this.climbing.finish_time = this.todate + "T" + this.totime + "Z";
      // console.log(this.climbing);
      // console.log(this.fromtime, this.fromdate);
      // console.log(this.totime, this.todate);
      // console.log(this.selected_peak);
      this.axios
        .post("//127.0.0.1:9000/climbings/create", this.climbing)
        .then((response) => {
          console.log(response);
          if (response.status == 201) {
            window.location = "/";
          }
        });
    },
  },
};
</script>

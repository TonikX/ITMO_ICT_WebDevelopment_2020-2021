<template>
  <v-form class="mb-footer">
    <v-container>
      <v-card class="my-5">
        <v-card-title>Create a peak</v-card-title>

        <v-col>
          <v-text-field
            v-model="peak.name"
            :rules="nameRules"
            :counter="80"
            label="Peak name"
            required
            outlined
            clearable
          ></v-text-field>
        </v-col>
        <v-col>
          <v-text-field
            v-model="peak.country"
            :rules="countryRules"
            :counter="56"
            label="Country"
            required
            outlined
            clearable
          ></v-text-field>
        </v-col>

        <v-col>
          <v-text-field
            v-model="peak.height"
            label="Height in meters"
            :rules="reqRules"
            required
            outlined
            clearable
          ></v-text-field>
        </v-col>
        <v-col>
          <v-text-field
            v-model="peak.climbing_duration"
            label="Climbing duration in hours"
            :rules="reqRules"
            required
            outlined
            clearable
          ></v-text-field>
        </v-col>
        <v-col>
          <v-textarea
            v-model="peak.route_description"
            clearable
            clear-icon="mdi-close-circle"
            label="Route description"
            placeholder="1 day - Arriving to the country. 2 day - Parking in the camp 1 (2500 m) 3 day - Adaptation"
          ></v-textarea>
        </v-col>
        <v-row justify="space-around" class="pb-5">
          <v-btn outlined large class="text-center" @click="postObj">
            Сохранить!
          </v-btn></v-row
        >
      </v-card>
    </v-container>
  </v-form>
</template>
<script>
export default {
  name: "CreatePeak",
  mounted() {
    this.getContext();
  },
  data: () => ({
    peak: {
      name: "",
      country: "",
      height: "",
      climbing_duration: "",
      route_description: "",
    },
    nameRules: [
      (v) => !!v || "Name is required",
      (v) =>
        v.length <= 80 || "Name of the club must be less then 80 characters",
    ],
    countryRules: [
      (v) => !!v || "Country is required",
      (v) => v.length <= 56 || "The longest country's name is 56 symbols long",
    ],
    reqRules: [(v) => !!v || "This field is required"],
  }),
  mounted() {
    this.getContext();
  },
  methods: {
    getContext() {
      console.log(this.$route);
      this.axios
        .get("//127.0.0.1:9000/peaks/" + this.$route.params.pk)
        .then((response) => {
          console.log(response, "responce");
          this.peak = response.data;
        });
    },
    postObj() {
      console.log(this.peak);
      let clubid = 0;
      this.axios
        .put("//127.0.0.1:9000/peaks/" + this.$route.params.pk, this.peak)
        .then((response) => {
          console.log(response);
        });
    },
  },
};
</script>
<template>
  <v-container>
    <v-row class="mt-5">
      <v-col cols="6" class="mx-auto">
        <v-img
          aspect-ratio="2"
          src="https://www.mensjournal.com/wp-content/uploads/2018/11/Climbers-Portaledge-GettyImages-961182248.jpg?w=900&quality=86&strip=all&iswp=1"
        ></v-img>
        <v-list dark color="mycolor">
          <v-list-group :value="false" prepend-icon="mdi-account">
            <template v-slot:activator>
              <v-list-item-title>Climber</v-list-item-title>
            </template>

            <v-list-item link :href="'climbers'">
              <v-list-item-title>View list</v-list-item-title
              ><v-list-item-icon
                ><v-icon>mdi-view-list</v-icon></v-list-item-icon
              >
            </v-list-item>

            <v-list-item link :href="'climbers/create'">
              <v-list-item-title>Add new</v-list-item-title
              ><v-list-item-icon><v-icon>mdi-plus</v-icon></v-list-item-icon>
            </v-list-item>

            <v-list-group :value="false" no-action sub-group>
              <template v-slot:activator>
                <v-list-item-content>
                  <v-list-item-title
                    >Edit</v-list-item-title
                  > </v-list-item-content
                ><v-list-item-icon
                  ><v-icon>mdi-pencil</v-icon></v-list-item-icon
                >
              </template>
              <v-list-item
                v-for="climber in climbers"
                :key="climber.id"
                link
                :href="climber.route"
              >
                <v-list-item-title>{{
                  climber.first_name +
                  " " +
                  climber.last_name +
                  ", id = " +
                  climber.id
                }}</v-list-item-title>
              </v-list-item>
            </v-list-group>
          </v-list-group>
        </v-list>
      </v-col>
      <v-col cols="6" class="mx-auto">
        <v-img
          aspect-ratio="2"
          src="https://c.stocksy.com/a/2j3900/z9/2159276.jpg"
          gradient="to top, rgba(50,40,35,.5), rgba(200,150,160,.1)"
        ></v-img>
        <v-list dark color="mycolor">
          <v-list-group :value="false" prepend-icon="mdi-image-filter-hdr">
            <template v-slot:activator>
              <v-list-item-title>Peak</v-list-item-title>
            </template>
            <v-list-item link :href="'peaks/'">
              <v-list-item-title>View list</v-list-item-title
              ><v-list-item-icon
                ><v-icon>mdi-view-list</v-icon></v-list-item-icon
              >
            </v-list-item>
            <v-list-item link :href="'peaks/no_climbings'">
              <v-list-item-title>List without climbings</v-list-item-title
              ><v-list-item-icon
                ><v-icon>mdi-filter-variant</v-icon></v-list-item-icon
              >
            </v-list-item>
            <v-list-item link :href="'peaks/create'">
              <v-list-item-title>Add new</v-list-item-title
              ><v-list-item-icon><v-icon>mdi-plus</v-icon></v-list-item-icon>
            </v-list-item>

            <v-list-group :value="false" no-action sub-group>
              <template v-slot:activator>
                <v-list-item-content>
                  <v-list-item-title
                    >Edit</v-list-item-title
                  > </v-list-item-content
                ><v-list-item-icon
                  ><v-icon>mdi-pencil</v-icon></v-list-item-icon
                >
              </template>
              <v-list-item
                v-for="peak in peaks"
                :key="peak.id"
                link
                :href="peak.route"
              >
                <v-list-item-title>{{
                  peak.name + " (" + peak.height + " м.) - " + peak.country
                }}</v-list-item-title>
              </v-list-item>
            </v-list-group>
          </v-list-group>
        </v-list>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12">
        <v-img
          aspect-ratio="2"
          src="https://miro.medium.com/max/1000/0*YgVdYhvfCh-YDgmc"
          gradient="to top, rgba(70,40,35,.5), rgba(200,150,160,.1)"
        ></v-img>
        <v-list dark color="mycolor">
          <v-list-group :value="false" prepend-icon="mdi-trending-up">
            <template v-slot:activator>
              <v-list-item-title>Climbing</v-list-item-title>
            </template>
            <v-list-item link :href="'climbings/'">
              <v-list-item-title>View list</v-list-item-title
              ><v-list-item-icon
                ><v-icon>mdi-view-list</v-icon></v-list-item-icon
              >
            </v-list-item>
            <v-list-item link :href="'climbings/create'">
              <v-list-item-title>Add new</v-list-item-title
              ><v-list-item-icon><v-icon>mdi-plus</v-icon></v-list-item-icon>
            </v-list-item>
          </v-list-group>
        </v-list>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-img
          aspect-ratio="2"
          src="https://res.cloudinary.com/dt84tw7zr/image/fetch/f_auto,q_auto/https://www.gameplan-a.com/wp-content/uploads/fly-images/12131/Team-top-of-the-mountain-climbing-640x9999.jpg"
        ></v-img>
        <v-list dark color="mycolor" class="mb-footer">
          <v-list-item link :href="'participations/create'">
            <v-list-item-icon
              ><v-icon>mdi-account-group</v-icon></v-list-item-icon
            >
            <v-list-item-title>Make a group</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-col>
      <v-col>
        <v-img
          aspect-ratio="2"
          src="https://airbus-h.assetsadobe2.com/is/image/content/dam/channel-specific/website-/stories/mountain-rescue/H145_SN20079_ADAC_M%C3%BCnchen_Harlaching_2017_12_14_106.jpg?wid=1920&fit=fit,1&qlt=85,0&fmt=png-alpha"
          gradient="to top, rgba(70,40,35,.5), rgba(200,150,160,.1)"
        ></v-img>
        <v-list dark color="mycolor" class="mb-footer">
          <v-list-item link :href="'emergencies/create'">
            <v-list-item-icon
              ><v-icon>mdi-car-brake-alert</v-icon></v-list-item-icon
            >
            <v-list-item-title>Add info about an emergency</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "HomePage",
  data: () => ({
    admins: [
      ["Management", "mdi-account-multiple-outline"],
      ["Settings", "mdi-cog-outline"],
    ],
    cruds: [
      ["Create", "mdi-plus-outline"],
      ["Read", "mdi-file-outline"],
      ["Update", "mdi-update"],
      ["Delete", "mdi-delete"],
    ],
    climbers: Object,
    peaks: Object,
  }),
  mounted() {
    this.getContext();
  },
  methods: {
    getContext() {
      this.axios
        .get("//127.0.0.1:9000/climbers/")
        .then((response) => {
          console.log(response.data);
          this.climbers = response.data;
          this.climbers.forEach((climber) => {
            climber.route = "climbers/" + climber.id;
          });
        })
        .catch((error) => console.log(error.response.data));
      this.axios
        .get("//127.0.0.1:9000/peaks/")
        .then((response) => {
          console.log(response.data);
          this.peaks = response.data;
          this.peaks.forEach((peak) => {
            peak.route = "peaks/" + peak.id;
          });
        })
        .catch((error) => console.log(error.response.data));
    },
  },
};
</script>

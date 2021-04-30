<template>
  <v-form v-model="valid" class="mb-footer">
    <v-container>
      <v-card class="my-5">
        <v-card-title>Create a climber</v-card-title>

        <v-col>
          <v-text-field
            v-model="first_name"
            :rules="nameRules"
            :counter="30"
            placeholder="Иван"
            label="First name"
            required
            outlined
            clearable
          ></v-text-field>
        </v-col>
        <v-col>
          <v-text-field
            v-model="last_name"
            :rules="nameRules"
            :counter="30"
            placeholder="Иванов"
            label="Last name"
            required
            outlined
            clearable
          ></v-text-field>
        </v-col>

        <v-col>
          <v-text-field
            v-model="address"
            :rules="addressRules"
            :counter="200"
            label="Address"
            required
            outlined
            clearable
          ></v-text-field>
        </v-col>
        <v-col>
          <v-select
            v-model="club"
            :items="club_names"
            label="Club"
            outlined
          ></v-select>
        </v-col>
        <v-col>
          <v-btn outlined large class="text-center" @click="postObj">
            Создать!
          </v-btn></v-col
        >
      </v-card>
    </v-container>
  </v-form>
</template>
<script>
export default {
  name: "CreateClimber",
  data: () => ({
    valid: false,
    clubs: Object,
    club_names: [],
    first_name: "",
    last_name: "",
    nameRules: [
      (v) => !!v || "Name is required",
      (v) => v.length <= 30 || "Name must be less than 30 characters",
    ],
    address: "",
    addressRules: [
      (v) => !!v || "E-mail is required",
      (v) => v.length <= 200 || "Address must be less than 200 characters",
    ],
    club: "",
  }),
  mounted() {
    this.getContext();
  },
  methods: {
    getContext() {
      this.axios.get("//127.0.0.1:9000/clubs/").then((response) => {
        console.log(response.data);
        this.clubs = response.data;
        this.clubs.forEach((club) => {
          this.club_names.push(club.name);
        });
      });
    },
    postObj() {
      console.log(this.first_name, this.last_name, this.address, this.club);
      let clubid = 0;
      this.clubs.forEach((club_obj) => {
        if (club_obj.name == this.club) {
          clubid = club_obj.id;
        }
      });
      let obj = {
        first_name: this.first_name,
        last_name: this.last_name,
        address: this.address,
        club: clubid,
      };
      console.log(obj);
      this.axios
        .post("//127.0.0.1:9000/climbers/create", obj)
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
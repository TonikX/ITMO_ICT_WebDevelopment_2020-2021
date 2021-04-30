<template>
  <v-card class="mt-5">
    <v-container v-if="mytoken != null"
      ><v-card-title>My account info</v-card-title>
      <!-- <v-card-text>My token is {{ mytoken }}</v-card-text> -->
    </v-container>

    <v-form v-if="mytoken != null" class="mb-footer"
      ><v-row justify="center"
        ><v-col cols="10">
          <v-text-field
            readonly
            v-model="username"
            label="Username"
            placeholder="username"
            :rules="[rules.required]"
          >
            HELLOMELLO
          </v-text-field></v-col
        >
        <!-- <v-col cols="10">
          <v-text-field
            v-model="first_name"
            label="First name"
            placeholder="First name"
            :rules="[rules.required]"
          >
            HELLOMELLO
          </v-text-field></v-col
        >
        <v-col cols="10">
          <v-text-field
            v-model="last_name"
            label="Last name"
            placeholder="Last name"
            :rules="[rules.required]"
          >
            HELLOMELLO
          </v-text-field></v-col
        > -->
        <v-col cols="10">
          <v-text-field
            v-model="email"
            label="E-mail"
            placeholder="mymail@mail.com"
            :rules="[rules.required]"
          >
            HELLOMELLO
          </v-text-field></v-col
        >
      </v-row>
      <v-row justify="center">
        <v-btn large outlined class="my-5 mr-5" @click="saveAccount"
          >Save changes!</v-btn
        ><v-btn large outlined class="my-5" @click="logout"
          >Log out!</v-btn
        ></v-row
      >
    </v-form>
    <!-- lalala -->

    <v-container v-if="mytoken == null"
      ><v-card-title>Hello!</v-card-title>
      <v-card-text
        >Now you are not authenticated, you need to choose an
        action:</v-card-text
      >
      <v-row justify="space-around"
        ><v-col cols="4">
          <v-img
            max-height="200"
            contain
            src="http://static.demilked.com/wp-content/uploads/2014/05/climbing-adopted-cat-craig-armstrong-millie-21.jpg"
          ></v-img></v-col
        ><v-col cols="5">
          <v-img
            max-height="200"
            contain
            src="https://www.treehugger.com/thmb/n2WSJdmXUJzY_d5m-BGN6mdGHfo=/644x364/filters:fill(auto,1)/__opt__aboutcom__coeus__resources__content_migration__mnn__images__2015__03__Millie_main-884dc19f04a8487e9ad64f9c3ee0841a.jpg"
          ></v-img></v-col
        ><v-col cols="3">
          <v-img
            max-height="200"
            contain
            src="https://static.boredpanda.com/blog/wp-content/uploads/2014/05/millie-climbing-cat-craig-armstrong-22.jpg"
          ></v-img
        ></v-col> </v-row
      ><v-row justify="center">
        <v-btn large outlined to="account/register" class="my-5 mr-5"
          >Register!</v-btn
        >
        <v-btn large outlined to="account/login" class="my-5"
          >Login!</v-btn
        ></v-row
      >
    </v-container>
  </v-card>
</template>

<script>
export default {
  data: () => ({
    mytoken: null,
    username: "",
    first_name: "",
    last_name: "",
    email: "",
    rules: {
      required: (value) => !!value || "Required.",
    },
  }),
  mounted() {
    this.mytoken = sessionStorage.getItem("auth_token");
    if (this.mytoken != null) {
      console.log("Token " + this.mytoken);
      this.axios
        .get("//127.0.0.1:9000/auth/users/me/", {
          headers: {
            Authorization: "Token " + this.mytoken,
          },
        })
        .then((response) => {
          console.log(response);
          this.username = response.data.username;
          this.email = response.data.email;
        });
    }
  },
  methods: {
    logout() {
      console.log(this.mytoken);
      sessionStorage.removeItem("auth_token");
      this.mytoken = null;
      console.log(this.mytoken);
      window.location = "/account";
    },
    saveAccount() {
      console.log("save changes");
      this.axios
        .patch(
          "//127.0.0.1:9000/auth/users/me/",
          { email: this.email },
          {
            headers: {
              Authorization: "Token " + this.mytoken,
            },
          }
        )
        .then((response) => {
          if (response.status == 200) {
            alert("success!");
          }
        });
    },
  },
};
</script>
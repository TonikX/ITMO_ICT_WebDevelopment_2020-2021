<template>
  <v-container fluid fill-height>
    <v-layout align-center justify-center>
      <v-flex xs12 sm8 md4 fill-height>
        <v-card class="elevation-12">
          <v-toolbar color="primary" dark>
            <v-toolbar-title>Register form</v-toolbar-title>
          </v-toolbar>
          <v-card-text>
            <v-form>
              <v-text-field name="login" label="Login" type="text"></v-text-field>
              <v-text-field id="password" name="password" label="Password" type="password"></v-text-field>
              <v-text-field name="First Name" label="First Name" type="text"></v-text-field>
              <v-text-field name="Last Name" label="Last Name" type="text"></v-text-field>
              <v-text-field name="email" label="Email" type="text"></v-text-field>
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="primary" dark to="/">Signup</v-btn>
          </v-card-actions>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  name: "Register",
};
</script>

<style></style>

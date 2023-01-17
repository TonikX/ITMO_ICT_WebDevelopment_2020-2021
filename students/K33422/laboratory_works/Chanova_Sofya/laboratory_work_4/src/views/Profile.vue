<template>
      <v-container fluid>
        <v-layout column>
            <h1>Profile Information</h1>
            <v-card>
                <v-card-text>
                    <v-text-field
                        outlined
                        readonly
                        v-model="userInfoDet.first_name"
                        label="First Name"></v-text-field>
                    <v-text-field
                        outlined
                        readonly
                        v-model="userInfoDet.last_name"
                        label="Last Name"></v-text-field>
                    <v-text-field
                        outlined
                        readonly
                        v-model="userInfoDet.email"
                        label="Email Address"></v-text-field>
                    <v-text-field
                        outlined
                        readonly
                        v-if="role == 's'"
                        v-model="userInfoDet.role"
                        label="Role">Student</v-text-field>
                    <v-text-field
                        outlined
                        readonly
                        v-if="role == 'd'"
                        v-model="userInfoDet.role"
                        label="Role">Dispatcher</v-text-field>
                    <v-text-field
                        outlined
                        readonly
                        v-if="role == 't'"
                        v-model="userInfoDet.role"
                        label="Role">Teacher</v-text-field>
                    <v-text-field
                        outlined
                        readonly
                        v-if="role == 's'"
                        v-model="userInfoDet.student_group "
                        label="Group"></v-text-field>
                    <v-text-field
                        outlined
                        readonly
                        v-if="role == 't'"
                        v-model="userInfoDet.teacher_qualification"
                        label="Qualification"></v-text-field>
                </v-card-text>
            </v-card>
        </v-layout>
              <v-btn v-if='auth'
             class="ma-2"
             dark
            href="/profile/edit"><v-icon
                              dark
                              left> mdi-account-edit</v-icon>Edit Profile</v-btn>
    </v-container>
</template>

<script>
export default {
  name: 'Profile',
  data: () => ({
    userInfoDet: [],
    role: localStorage.getItem('role')
  }),
  created () {
    this.userInfo()
    this.getRole()
  },
  computed: {
    auth () {
      if (localStorage.getItem('token')) {
        return true
      } else {
        return false
      }
    }
  },
  methods: {
    async userInfo () {
      try {
        const response = await this.axios
          .get('http://localhost:8000/college/profile/' + localStorage.getItem('username'),
            {
              headers: {
                Authorization: 'Token ' + localStorage.getItem('token'),
                'Content-Type': 'application/json'
              }
            })

        // if (response.status !== 200) {
        //   throw new Error(response.status)
        // }
        // window.location.reload()
        this.userInfoDet = response.data
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    }
  }
}
</script>

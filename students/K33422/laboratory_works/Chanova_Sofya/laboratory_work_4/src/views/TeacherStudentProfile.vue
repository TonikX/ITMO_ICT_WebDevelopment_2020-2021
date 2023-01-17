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
                        v-if="account_role == 'student'"
                        v-model="userInfoDet.role"
                        label="Role">Student</v-text-field>
                    <v-text-field
                        outlined
                        readonly
                        v-if="account_role == 'dispatcher'"
                        v-model="userInfoDet.role"
                        label="Role">Dispatcher</v-text-field>
                    <v-text-field
                        outlined
                        readonly
                        v-if="account_role == 'teacher'"
                        v-model="userInfoDet.role"
                        label="Role">Teacher</v-text-field>
                    <v-text-field
                        outlined
                        readonly
                        v-if="account_role == 'student'"
                        v-model="userInfoDet.student_group "
                        label="Group"></v-text-field>
                    <v-text-field
                        outlined
                        readonly
                        v-if="account_role == 'teacher'"
                        v-model="userInfoDet.teacher_qualification"
                        label="Qualification"></v-text-field>
                </v-card-text>
            </v-card>
        </v-layout>
    </v-container>
</template>

<script>
export default {
  name: 'Account',
  data: () => ({
    userInfoDet: [],
    account_role: localStorage.getItem('role_click')
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
          .get('http://localhost:8000/college/profile/' + localStorage.getItem('username_click'),
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

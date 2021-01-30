<template>
    <v-container fluid>
        <v-layout column>
            <v-card>
                <v-card-text>
                    <v-text-field
                        v-model="userInfoDet.first_name"
                        label="First Name"></v-text-field>
                    <v-text-field
                        v-model="userInfoDet.last_name"
                        label="Last Name"></v-text-field>
                    <v-text-field
                        v-model="userInfoDet.passport"
                        label="Passport"></v-text-field>
                </v-card-text>
                <v-card-actions>
                    <v-btn color="white" v-if='auth' @click="edit">
                        Save Changes
                    </v-btn>
                </v-card-actions>
            </v-card>
        </v-layout>
    </v-container>
</template>

<script>
export default {
  name: 'UserInfo',
  data: () => ({
    profileForm: [],
    userInfoDet: []
  }),
  created () {
    this.userInfo()
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
          .get('http://127.0.0.1:8000/auth/users/me/',
            {
              headers: {
                Authorization: 'Token ' + localStorage.getItem('token'),
                'Content-Type': 'application/json'
              }
            })
        this.userInfoDet = response.data
        this.profileForm = response.data
        return response.data
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },

    async edit () {
      try {
        const response = await this.axios
          .patch('http://127.0.0.1:8000/auth/users/me/', JSON.stringify(this.profileForm),
            {
              headers: {
                Authorization: 'Token ' + localStorage.getItem('token'),
                'Content-Type': 'application/json'
              }
            })

        console.log('EDIT PROFILE RESPONSE', response)

        this.$router.push('/settings')
        this.$router.go()
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    }
  }
}
</script>

<template>
  <v-card>
    <v-card-title>
      Teachers' accounts
      <v-spacer></v-spacer>
    </v-card-title>
    <v-data-table
      :headers="headers"
      :items="teachers"
      :search="search"
      class="elevation-1"
    >
      <template v-slot:item="row">
            <tr>
              <td>{{row.item.first_name}}</td>
              <td>{{row.item.last_name}}</td>
              <td>{{row.item.username}}</td>
              <td>
                  <v-btn class="mx-2" fab dark small color="pink" @click="onButtonClick(row.item)">
                      <v-icon dark>mdi-account-edit</v-icon>
                  </v-btn>
              </td>
            </tr>
        </template>
    </v-data-table>
  </v-card>
</template>

<script>

export default {
  data: () => ({
    isAuth: '',
    dialog: false,
    dialogDelete: false,
    flag: false,
    headers: [
      { text: 'First name', value: 'first_name' },
      { text: 'Last name', value: 'last_name' },
      { text: 'Username', value: 'username' },
      { text: '', value: 'action' }],

    teachers: []
  }),

  computed: {
    formTitle () {
      return this.editedIndex === -1 ? 'New Item' : 'Edit Item'
    }
  },

  created () {
    this.teachersList()
  },

  methods: {
    async teachersList () {
      try {
        const response = await this.axios
          .get('http://localhost:8000/college/teachers')

        if (response.status !== 200) {
          throw new Error(response.status)
        }
        this.teachers = response.data
        return response.data
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    onButtonClick (item) {
      localStorage.setItem('role_click', item.role)
      localStorage.setItem('username_click', item.username)
      this.$router.push('/account')
    }
  }
}
</script>

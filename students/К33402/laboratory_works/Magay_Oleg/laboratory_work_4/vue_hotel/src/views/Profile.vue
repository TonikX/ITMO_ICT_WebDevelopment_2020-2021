<template>
  <div class="home">
    <h3>Личный кабинет</h3>
    <table>
      <tr>
        <td><strong>Email</strong></td>
        <td>
          {{ user.email }}
          <v-btn small @click="changeState">Edit</v-btn>
        </td>
      </tr>
      <tr>
        <td><strong>Username</strong></td>
        <td>{{ user.username }}</td>
      </tr>
    </table>
    <v-form
      v-if="state"
      @submit.prevent="update"
      ref="addForm"
      class="my-2">
      <v-row>
        <v-col cols="5" class="mx-auto">
          <v-text-field
            label="Введите email"
            v-model="addForm.email"
          />
          <v-btn small color="primary" @click="update">update</v-btn>
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>

<script>
export default {
  name: 'Profile',
  data: () => ({
    user: {},
    state: false,
    addForm: {
      email: ''
    }
  }),
  async created () {
    await this.axios
      .get('http://127.0.0.1:8000/auth/users/me/')
      .then((res) => {
        this.user = res.data
        console.log(this.user)
      })
      .catch((error) => {
        console.log(error)
      })
  },
  methods: {
    changeState () {
      this.state = !this.state
    },
    async update (el) {
      await this.axios
        .put('http://127.0.0.1:8000/auth/users/me/', this.addForm)
        .then((res) => {
          console.log(res)
          this.$router.go()
        })
        .catch((error) => {
          console.log(error)
          alert('Похоже, вы ввели некорректный email!')
        })
    }
  }
}
</script>

<style scoped>
  table {
    width: 50%;
  }
  td {
    text-align: left;
    padding: 0.5rem;
  }
  button {
    margin-left: 40px;
  }
  h3 {
    margin-bottom: 50px;
  }
</style>

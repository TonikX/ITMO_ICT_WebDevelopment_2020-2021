<template>
  <div>
    <ul class="ttxt">
      <h1>Список посетителей</h1>
      <ul class="greeting-list">
        <li
          v-for="guest in guests"
          :key="guest.number"
        >
          {{ guest.id }} - {{ guest.name }} {{ guest.surname }} - {{ guest.room }} room
        </li>
      </ul>
      <ul class="bttns">
        <v-btn
          color="#252526"
          dark
          @click="dialog = true"
        >
          Изменить
        </v-btn>
      </ul>
    </ul>
    <v-row>
      <v-dialog
        v-model="dialog"
        persistent
        max-width="600px"
      >
        <v-card>
          <v-card-title>
            <span class="headline">Guest info</span>
            <v-spacer></v-spacer>
            <v-btn
              icon
              @click="dialog = false"
            >
              <v-icon>mdi-close</v-icon>
            </v-btn>
          </v-card-title>
          <v-card-text>
            <v-container>
              <v-row>
                <v-col
                  cols="12"
                  sm="6"
                  md="4"
                >
                  <v-text-field
                    v-model="guestId"
                    label="ID"
                    required
                  ></v-text-field>
                </v-col>
                <v-col
                  cols="12"
                  sm="6"
                  md="4"
                >
                  <v-text-field
                    label="Номер паспорта"
                    persistent-hint
                    required
                    v-model="passportNumber"
                  ></v-text-field>
                </v-col>
                <v-col cols="12" sm="6"
                       md="4">
                  <v-text-field
                    label="Имя"
                    required
                    v-model="name"
                  ></v-text-field>
                </v-col>
                <v-col cols="12" sm="6"
                       md="4">
                  <v-text-field
                    label="Фамилия"
                    required
                    v-model="surname"
                  ></v-text-field>
                </v-col>
                <v-col cols="12" sm="6"
                       md="4">
                  <v-text-field
                    label="Отчество"
                    required
                    v-model="middlename"
                  ></v-text-field>
                </v-col>
                <v-col cols="12" sm="6"
                       md="4">
                  <v-text-field
                    label="Место рождения"
                    required
                    v-model="fromLocation"
                  ></v-text-field>
                </v-col>
                <v-col cols="12" sm="6"
                       md="4">
                  <v-text-field
                    label="Дата прибытия"
                    required
                    v-model="checkInDate"
                    type="date"
                  ></v-text-field>
                </v-col>
                <v-col cols="12" sm="6"
                       md="4">
                  <v-text-field
                    label="Номер"
                    required
                    v-model="room"
                  ></v-text-field>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn icon @click="search">
              <v-icon>mdi-magnify</v-icon>
            </v-btn>
            <v-btn
              color="cancel"
              text
              @click="doDelete"
            >
              Delete
            </v-btn>
            <v-btn
              color="info"
              text
              @click="update"
            >
              Update
            </v-btn>
            <v-btn
              color="success"
              text
              @click="add"
            >
              Add
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-row>
  </div>
</template>

<script>
export default {
  name: 'Guests',
  data: () => ({
    guests: [],
    dialog: false,
    guestId: '',
    passportNumber: '',
    name: '',
    surname: '',
    middlename: '',
    fromLocation: '',
    checkInDate: '',
    room: ''
  }),
  methods: {
    search () {
      const guest = this.guests.filter(guest => guest.id === Number.parseInt(this.guestId))[0]
      if (guest) {
        this.guestId = guest.id
        this.passportNumber = guest.passport_number
        this.name = guest.name
        this.surname = guest.surname
        this.middlename = guest.middlename
        this.fromLocation = guest.from_location
        this.checkInDate = guest.check_in_date
        this.room = guest.room
      } else {
        this.guestId = ''
        this.passportNumber = ''
        this.name = ''
        this.surname = ''
        this.middlename = ''
        this.fromLocation = ''
        this.checkInDate = ''
        this.room = ''
      }
    },
    async add () {
      const body = {
        passport_number: this.passportNumber,
        name: this.name,
        surname: this.surname,
        middlename: this.middlename,
        from_location: this.fromLocation,
        check_in_date: this.checkInDate,
        room: this.room
      }
      const response = await this.axios.post(this.$hostname + 'hotel/guests/',
        body,
        {
          headers:
            {
              Authorization: 'Token ' + localStorage.getItem('auth_token')
            }
        }
      )
      console.log(response)
      this.dialog = false
      if (response.status === 201) {
        this.guests.push(body)
      }
    },
    async update () {
      const body = {
        passport_number: this.passportNumber,
        name: this.name,
        surname: this.surname,
        middlename: this.middlename,
        from_location: this.fromLocation,
        check_in_date: this.checkInDate,
        room: this.room
      }
      const response = await this.axios.patch(this.$hostname + 'hotel/guests/' + this.guestId + '/',
        body,
        {
          headers:
            {
              Authorization: 'Token ' + localStorage.getItem('auth_token')
            }
        }
      )
      console.log(response)
      this.guests = this.guests.filter(guest => guest.id !== Number.parseInt(this.guestId))
      if (response.status === 200) {
        body.id = this.guestId
        this.guests.push(body)
      }
      this.dialog = false
    },
    doDelete () {
      this.axios.delete(this.$hostname + 'hotel/guests/' + this.guestId + '/', { headers: { Authorization: 'Token ' + localStorage.getItem('auth_token') } })
        .then(response => {
          console.log(response)
        })
        .catch(error => {
          console.log(error)
        })
      this.guests = this.guests.filter(guest => guest.id !== Number.parseInt(this.guestId))
      this.dialog = false
    }
  },
  created () {
    this.axios.get(this.$hostname + 'hotel/guests/', { headers: { Authorization: 'Token ' + localStorage.getItem('auth_token') } })
      .then(response => {
        this.guests = response.data
      })
      .catch(error => {
        console.log(error)
      })
  }
}
</script>

<style scoped>

</style>

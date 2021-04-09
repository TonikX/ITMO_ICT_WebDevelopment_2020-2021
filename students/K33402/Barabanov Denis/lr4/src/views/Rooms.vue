<template>
  <div>
    <ul class="ttxt">
      <h1>Список <span v-if="filter">свободных</span> номеров</h1>
      <ul class="greeting-list">
        <li
          v-for="room in filteredRooms"
          :key="room.number"
        >
          {{ room.number }} ({{room.type}}-х местный)
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
        <v-btn
          color="#252526"
          dark
          v-if="!filter"
          @click="filter = true"
          class="mx-2"
        >
          Свободные номера
        </v-btn>
        <v-btn
          color="#252526"
          dark
          v-if="filter"
          @click="filter = false"
          class="mx-2"
        >
          Все номера
        </v-btn>
      </ul>
    </ul>
    <v-row>
      <v-dialog
        v-model="dialog"
        persistent
        max-width="800px"
      >
        <v-card>
          <v-card-title>
            <span class="headline">Информация о номере</span>
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
                    v-model="roomNumber"
                    label="Номер комнаты"
                    required
                  ></v-text-field>
                </v-col>
                <v-col
                  cols="12"
                  sm="6"
                  md="4"
                >
                  <v-select v-model="roomType"
                            :items="['1', '2', '3']"
                            label="Вместимость"
                  ></v-select>
                </v-col>
                <v-col
                  cols="12"
                  sm="6"
                  md="4"
                >
                  <v-text-field
                    label="Цена"
                    persistent-hint
                    required
                    v-model="roomPrice"
                  ></v-text-field>
                </v-col>
                <v-col cols="12" sm="6"
                       md="4">
                  <v-text-field
                    label="Этаж"
                    required
                    v-model="roomFloor"
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
  name: 'Rooms',
  data: () => ({
    rooms: [],
    busyRooms: [],
    filter: false,
    dialog: false,
    roomType: '',
    roomPrice: '',
    roomNumber: '',
    roomFloor: ''
  }),
  methods: {
    search () {
      console.log(this.rooms)
      const room = this.rooms.filter(room => room.number === Number.parseInt(this.roomNumber))[0]
      if (room) {
        this.roomType = room.type
        this.roomPrice = room.price
        this.roomFloor = room.floor
      } else {
        this.roomType = ''
        this.roomPrice = ''
        this.roomFloor = ''
      }
    },
    async add () {
      const body = {
        number: this.roomNumber,
        type: this.roomType,
        price: this.roomPrice,
        floor: this.roomFloor
      }
      const response = await this.axios.post(this.$hostname + 'hotel/rooms/',
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
        this.rooms.push(body)
      }
    },
    async update () {
      const body = {
        type: this.roomType,
        price: this.roomPrice,
        floor: this.roomFloor
      }
      const response = await this.axios.patch(this.$hostname + 'hotel/rooms/' + this.roomNumber + '/',
        body,
        {
          headers:
            {
              Authorization: 'Token ' + localStorage.getItem('auth_token')
            }
        }
      )
      console.log(response)
      this.rooms = this.rooms.filter(room => room.number !== Number.parseInt(this.roomNumber))
      if (response.status === 200) {
        body.number = this.roomNumber
        this.rooms.push(body)
      }
      this.dialog = false
    },
    doDelete () {
      this.axios.delete(this.$hostname + 'hotel/rooms/' + this.roomNumber + '/', { headers: { Authorization: 'Token ' + localStorage.getItem('auth_token') } })
        .then(response => {
          console.log(response)
        })
        .catch(error => {
          console.log(error)
        })
      this.rooms = this.rooms.filter(room => room.number !== Number.parseInt(this.roomNumber))
      this.dialog = false
    }
  },
  computed: {
    filteredRooms () {
      if (this.filter) {
        return this.rooms.filter(room => !this.busyRooms.includes(room.number))
      }
      return this.rooms
    }
  },
  created () {
    this.axios.get(this.$hostname + 'hotel/rooms/', { headers: { Authorization: 'Token ' + localStorage.getItem('auth_token') } })
      .then(response => {
        this.rooms = response.data
      })
      .catch(error => {
        console.log(error)
      })
    this.axios.get(this.$hostname + 'hotel/guests/', { headers: { Authorization: 'Token ' + localStorage.getItem('auth_token') } })
      .then(response => {
        this.busyRooms = response.data.map(guest => guest.room)
        console.log(this.busyRooms)
      })
      .catch(error => {
        console.log(error)
      })
  }
}
</script>

<style>
.greeting-list {
  list-style-position: inside ;
  float: center;
  box-sizing: border-box;
  font-size: 120%;
}
.bttns {
  margin-top: 2%;
}
</style>

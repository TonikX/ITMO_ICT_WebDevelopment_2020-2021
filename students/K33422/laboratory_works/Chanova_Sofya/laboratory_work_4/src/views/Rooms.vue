<template>
  <v-data-table
    :headers="headers"
    :items="rooms"
    class="elevation-1"
  >
    <template v-slot:top>
      <v-toolbar
        flat
      >
        <v-toolbar-title>Rooms</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-dialog
          v-model="dialog"
          max-width="500px"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              dark
              class="mb-2"
              v-bind="attrs"
              v-on="on"
            >
              New Room
            </v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="headline">{{ formTitle }}</span>
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
                      type="number"
                      v-model.number="editedItem.id"
                      label="Room id"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      type="number"
                      v-model.number="editedItem.room_number"
                      label="Room number"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      type="number"
                      v-model.number="editedItem.seats_quantity"
                      label="Number of seats"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                  <v-select
                    :items="themes"
                    v-model='editedItem.subject_theme'
                    label="Subject theme"
                  ></v-select>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                color="blue darken-1"
                text
                @click="close"
              >
                Cancel
              </v-btn>
              <v-btn
                color="blue darken-1"
                text
                @click="save"
              >
                Save
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <v-dialog v-model="dialogDelete" max-width="500px">
          <v-card>
            <v-card-title class="headline">Are you sure you want to delete this item?</v-card-title>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="closeDelete">Cancel</v-btn>
              <v-btn color="blue darken-1" text @click="deleteItemConfirm">OK</v-btn>
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-toolbar>

    </template>
    <template v-slot:item.actions="{ item }">
      <v-icon
        small
        class="mr-2"
        @click="editItem(item)"
      >
        mdi-pencil
      </v-icon>
      <v-icon
        small
        @click="deleteItem(item)"
      >
        mdi-delete
      </v-icon>
    </template>
  </v-data-table>
</template>

<script>
import axios from 'axios'
export default {
  data: () => ({
    isAuth: '',
    dialog: false,
    dialogDelete: false,
    flag: false,
    headers: [
      {
        text: 'Rooms',
        align: 'start',
        sortable: false,
        value: 'name'
      },
      { text: 'Room id', value: 'id' },
      { text: 'Room number', value: 'room_number' },
      { text: 'Number of seats', value: 'seats_quantity' },
      { text: 'Subject theme', value: 'subject_theme' },
      { text: 'Actions', value: 'actions', sortable: false }
    ],
    rooms: [],
    themes: ['chemistry lab', 'computer class', 'hall', 'physics lab', 'none'],
    editedIndex: -1,
    editedItem: {
      id: 0,
      room_number: 0,
      seats_quantity: 0,
      subject_theme: ''
    },
    defaultItem: {
      id: 0,
      room_number: 0,
      seats_quantity: 0,
      subject_theme: ''
    }
  }),

  computed: {
    formTitle () {
      return this.editedIndex === -1 ? 'New Item' : 'Edit Item'
    }
  },

  watch: {
    dialog (val) {
      val || this.close()
    },
    dialogDelete (val) {
      val || this.closeDelete()
    }
  },

  created () {
    this.roomsList()
  },

  methods: {
    async roomsList () {
      try {
        const response = await this.axios
          .get('http://localhost:8000/college/rooms')

        if (response.status !== 200) {
          throw new Error(response.status)
        }
        this.rooms = response.data
        return response.data
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    editItem (item) {
      this.editedIndex = this.rooms.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialog = true
    },

    deleteItem (item) {
      this.editedIndex = this.rooms.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialogDelete = true
    },

    deleteItemConfirm () {
      if (this.editedIndex > -1) {
        this.rooms.splice(this.editedIndex, 1)
        this.closeDelete()
        axios.delete('http://localhost:8000/college/rooms/' + JSON.stringify(this.editedItem.id), {
          id: this.editedItem.id,
          room_number: +this.editedItem.room_number,
          seats_quantity: +this.editedItem.seats_quantity,
          subject_theme: this.editedItem.subject_theme
        })
      } else {
        this.rooms.push(this.editedItem)
      }
      this.close()
    },

    close () {
      this.dialog = false
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem)
        this.editedIndex = -1
      })
    },

    closeDelete () {
      this.dialogDelete = false
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem)
        this.editedIndex = -1
      })
    },
    transformOptions () {
      if (this.editedItem.subject_theme === 'chemistry lab') {
        this.editedItem.subject_theme = 'chl'
      } else if (this.editedItem.subject_theme === 'computer class') {
        this.editedItem.subject_theme = 'cc'
      } else if (this.editedItem.subject_theme === 'hall') {
        this.editedItem.subject_theme = 'h'
      } else if (this.editedItem.subject_theme === 'physics lab') {
        this.editedItem.subject_theme = 'phl'
      } else if (this.editedItem.subject_theme === 'none') {
        this.editedItem.subject_theme = 'n'
      }
    },
    async createRoom () {
      this.transformOptions()
      try {
        const response = await this.axios
          .post('http://localhost:8000/college/rooms/add/', {
            room_number: this.editedItem.room_number,
            seats_quantity: this.editedItem.seats_quantity,
            subject_theme: this.editedItem.subject_theme
          })

        if (response.status !== 201) {
          throw new Error(response.status)
        }

        window.location.reload()
      } catch (e) {
        console.error('API ERROR', e)
      }
    },
    async updateRoom () {
      this.transformOptions()
      this.editedIndex = 1
      try {
        const response = await this.axios
          .put('http://localhost:8000/college/rooms/' + JSON.stringify(this.editedItem.id) + '/', {
            id: this.editedItem.id,
            room_number: this.editedItem.room_number,
            seats_quantity: this.editedItem.seats_quantity,
            subject_theme: this.editedItem.subject_theme
          })

        if (response.status !== 200) {
          throw new Error(response.status)
        }

        window.location.reload()
      } catch (e) {
        console.error('API ERROR', e)
      }
    },
    save () {
      if (this.editedIndex > -1) {
        this.updateRoom()
      } else {
        this.createRoom()
      }
    }
  }
}
</script>

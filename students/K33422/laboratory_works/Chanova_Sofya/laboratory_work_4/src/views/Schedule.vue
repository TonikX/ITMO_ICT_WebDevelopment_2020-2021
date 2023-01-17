<template>
  <v-card>
    <v-card-title>
      Schedule
      <v-spacer></v-spacer>
      <v-text-field
        v-model="search"
        append-icon="mdi-magnify"
        label="Search"
        single-line
        hide-details
      ></v-text-field>
    </v-card-title>
    <v-data-table
    :headers="headers"
    :items="entries"
    class="elevation-1"
    :search="search"
  >
    <template v-slot:top>
      <v-toolbar
        flat
      >
                    {{ editedItem }}

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
              New entry
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
                      label="Id"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-select
                    :items="weekdays"
                    v-model='editedItem.weekday'
                    label="Weekday"
                    item-text="weekday"
                    item-value="weekday"
                  ></v-select>

                    <v-select
                    :items="lessons"
                    v-model='editedItem.time'
                    label="Time"
                    item-text="time"
                    item-value="time"
                  ></v-select>

                    <v-select
                    :items="rooms"
                    v-model='editedItem.room_number'
                    label="Room"
                    item-text="room_number"
                    item-value="room_number"
                  ></v-select>

                    <v-select
                    :items="groups"
                    v-model='editedItem.group_number'
                    label="Group"
                    item-text="group_number"
                    item-value="group_number"
                  ></v-select>
                    <v-select
                    :items="teachers"
                    v-model='editedItem.teacher'
                    label="Teacher"
                    item-text="username"
                    item-value="username"
                  ></v-select>

                    <v-select
                    :items="subjects"
                    v-model='editedItem.subject'
                    label="Subject"
                    item-text="subject_name"
                    item-value="subject_name"
                  ></v-select>

                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                dark
                color="blue darken-1"
                text
                @click="close"
              >
                Cancel
              </v-btn>
              <v-btn
                dark
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
  </v-card>
</template>

<script>
import axios from 'axios'
export default {
  data: () => ({
    search: '',
    isAuth: '',
    dialog: false,
    dialogDelete: false,
    flag: false,
    headers: [
      { text: 'Id', value: 'id' },
      { text: 'Weekday', value: 'weekday' },
      { text: 'Time', value: 'time' },
      { text: 'Room', value: 'room_number' },
      { text: 'Group', value: 'group_number' },
      { text: 'Teacher', value: 'teacher' },
      { text: 'Subject', value: 'subject' },
      { text: 'Actions', value: 'actions', sortable: false }
    ],
    entries: [],
    weekdays: ['Monday', 'Tuesday', 'Thursday', 'Wednesday', 'Friday', 'Saturday', 'Sunday'],
    lessons: ['8:20', '10:00', '11:40', '13:30', '15:20', '17:00', '18:40'],
    rooms: [],
    groups: [],
    teachers: [],
    subjects: [],
    editedIndex: -1,
    editedItem: {
      id: 0,
      weekday: 0,
      time: 0,
      room_number: 0,
      group_number: 0,
      teacher: 0,
      subject: 0
    },
    defaultItem: {
      id: 0,
      weekday: '',
      time: '',
      room_number: '',
      group_number: '',
      teacher: '',
      subject: ''
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
    this.entriesList()
    this.roomsList()
    this.groupsList()
    this.teachersList()
    this.subjectsList()
  },

  methods: {
    async entriesList () {
      try {
        const response = await this.axios
          .get('http://localhost:8000/college/schedule')

        if (response.status !== 200) {
          throw new Error(response.status)
        }
        this.entries = response.data
        return response.data
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    editItem (item) {
      this.editedIndex = this.entries.indexOf(item)
      console.log(this.subjects.find(item => item.username === this.editedItem.teacher).id)
      console.log(this.subjects.find(item => item => item.room_number === this.editedItem.room_number).id)
      console.log(this.subjects.find(item => item.group_number === this.editedItem.group_number).id)
      console.log(this.subjects.find(item => item.subject === this.editedItem.subject).id)
      this.editedItem = Object.assign({}, item)
      this.editedItem.teacher = this.teachers.find(item => item.username === this.editedItem.teacher).id
      this.editedItem.room_number = this.rooms.find(item => item.room_number === this.editedItem.room_number).id
      this.editedItem.group_number = this.groups.find(item => item.group_number === this.editedItem.group_number).id
      this.editedItem.subject = this.subjects.find(item => item.subject === this.editedItem.subject).id
      this.dialog = true
    },
    deleteItem (item) {
      this.editedIndex = this.entries.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialogDelete = true
    },

    deleteItemConfirm () {
      if (this.editedIndex > -1) {
        this.entries.splice(this.editedIndex, 1)
        this.closeDelete()
        axios.delete('http://localhost:8000/college/schedule/' + JSON.stringify(this.editedItem.id), {
          id: this.editedItem.id,
          room_number: +this.editedItem.room_number,
          seats_quantity: +this.editedItem.seats_quantity,
          subject_theme: this.editedItem.subject_theme
        })
      } else {
        this.entries.push(this.editedItem)
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
      if (this.editedItem.weekday === 'Monday') {
        this.editedItem.weekday = '0'
      } else if (this.editedItem.weekday === 'Tuesday') {
        this.editedItem.weekday = '1'
      } else if (this.editedItem.weekday === 'Wednesday') {
        this.editedItem.weekday = '2'
      } else if (this.editedItem.weekday === 'Thursday') {
        this.editedItem.weekday = '3'
      } else if (this.editedItem.weekday === 'Friday') {
        this.editedItem.weekday = '4'
      } else if (this.editedItem.weekday === 'Saturday') {
        this.editedItem.weekday = '5'
      } else if (this.editedItem.weekday === 'Sunday') {
        this.editedItem.weekday = '6'
      } else if (this.editedItem.time === '8:20') {
        this.editedItem.weekday = '0'
      } else if (this.editedItem.time === '10:00') {
        this.editedItem.weekday = '1'
      } else if (this.editedItem.time === '11:40') {
        this.editedItem.weekday = '2'
      } else if (this.editedItem.time === '13:30') {
        this.editedItem.weekday = '3'
      } else if (this.editedItem.time === '15:20') {
        this.editedItem.weekday = '4'
      } else if (this.editedItem.time === '17:00') {
        this.editedItem.weekday = '5'
      } else if (this.editedItem.time === '18:40') {
        this.editedItem.weekday = '6'
      }
    },
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

    async groupsList () {
      try {
        const response = await this.axios
          .get('http://localhost:8000/college/groups')

        if (response.status !== 200) {
          throw new Error(response.status)
        }
        this.groups = response.data
        return response.data
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },

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

    async subjectsList () {
      try {
        const response = await this.axios
          .get('http://localhost:8000/college/subjects')

        if (response.status !== 200) {
          throw new Error(response.status)
        }
        this.subjects = response.data
        return response.data
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },

    async createEntry () {
      this.transformOptions()
      try {
        const response = await this.axios
          .post('http://localhost:8000/college/schedule/add/', {
            time: this.editedItem.time,
            weekday: this.editedItem.weekday,
            room_number: this.editedItem.room_number,
            group_number: this.editedItem.group_number,
            teacher: this.editedItem.teacher,
            subject: this.editedItem.subject
          })

        if (response.status !== 201) {
          throw new Error(response.status)
        }

        window.location.reload()
      } catch (e) {
        console.error('API ERROR', e)
      }
    },
    async updateEntry () {
      this.transformOptions()
      this.editedIndex = 1
      try {
        const response = await this.axios
          .put('http://localhost:8000/college/schedule/' + JSON.stringify(this.editedItem.id) + '/', {
            time: this.editedItem.time,
            weekday: this.editedItem.weekday,
            room_number: this.editedItem.room_number,
            group_number: this.editedItem.group_number,
            teacher: this.editedItem.teacher,
            subject: this.editedItem.subject
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
        this.updateEntry()
      } else {
        this.createEntry()
      }
    }
  }
}
</script>

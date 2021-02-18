<template>
  <v-data-table
    :headers="headers"
    :items="groups"
    class="elevation-1"
  >
    <template v-slot:top>
      <v-toolbar
        flat
      >
        <v-toolbar-title>Groups</v-toolbar-title>
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
              New Group
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
                      label="Group id"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.group_number"
                      label="Group number"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      type="number"
                      v-model.number="editedItem.course_number"
                      label="Course"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.department"
                      label="Department"
                    ></v-text-field>
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
        text: 'Groups',
        align: 'start',
        sortable: false,
        value: 'name'
      },
      { text: 'Group id', value: 'id' },
      { text: 'Group number', value: 'group_number' },
      { text: 'Number of course', value: 'course_number' },
      { text: 'Department', value: 'department' },
      { text: 'Actions', value: 'actions', sortable: false }
    ],
    groups: [],
    editedIndex: -1,
    editedItem: {
      id: 0,
      group_number: 0,
      course_number: 0,
      department: ''
    },
    defaultItem: {
      id: 0,
      group_number: 0,
      course_number: 0,
      department: ''
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
    this.groupsList()
  },

  methods: {
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
    editItem (item) {
      this.editedIndex = this.groups.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialog = true
    },

    deleteItem (item) {
      this.editedIndex = this.groups.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialogDelete = true
    },

    deleteItemConfirm () {
      if (this.editedIndex > -1) {
        this.groups.splice(this.editedIndex, 1)
        this.closeDelete()
        axios.delete('http://localhost:8000/college/groups/' + JSON.stringify(this.editedItem.id), {
          id: this.editedItem.id,
          group_number: this.editedItem.group_number,
          course_number: +this.editedItem.course_number,
          department: this.editedItem.department
        })
      } else {
        this.groups.push(this.editedItem)
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
    async createGroup () {
      try {
        const response = await this.axios
          .post('http://localhost:8000/college/groups/add/', {
            group_number: this.editedItem.group_number,
            course_number: +this.editedItem.course_number,
            department: this.editedItem.department
          })

        if (response.status !== 201) {
          throw new Error(response.status)
        }

        window.location.reload()
      } catch (e) {
        console.error('API ERROR', e)
      }
    },
    async updateGroup () {
      this.editedIndex = 1
      try {
        const response = await this.axios
          .put('http://localhost:8000/college/groups/' + JSON.stringify(this.editedItem.id) + '/', {
            group_number: this.editedItem.group_number,
            course_number: +this.editedItem.course_number,
            department: this.editedItem.department
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
        this.updateGroup()
      } else {
        this.createGroup()
      }
    }
  }
}
</script>

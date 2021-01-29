<template>
  <v-data-table
    :headers="headers"
    :items="services"
    class="elevation-1"
  >
    <template v-slot:top>
      <v-toolbar
        flat
      >
        <v-toolbar-title>Services</v-toolbar-title>
        <v-divider
          class="mx-4"
          inset
          vertical
        ></v-divider>
        <v-spacer></v-spacer>
        <v-dialog
          v-model="dialog"
          max-width="500px"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              color="black"
              dark
              class="mb-2"
              v-bind="attrs"
              v-on="on"
            >
              New Item
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
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.title"
                      label="Title"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                  <v-select
                    :items="type_serviceList"
                    v-model='editedItem.type_service'
                    single-line
                    item-text='type_service'
                    item-value='type_service'
                    label="Type of service"
                  ></v-select>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.price"
                      label="Price"
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
                color="gray darken-1"
                text
                @click="close"
              >
                Cancel
              </v-btn>
              <v-btn
                color="gray darken-4"
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
              <v-btn color="gray darken-1" text @click="closeDelete">Cancel</v-btn>
              <v-btn color="gray darken-1" text @click="deleteItemConfirm">OK</v-btn>
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
    dialog: false,
    dialogDelete: false,
    headers: [
      {
        text: 'Services',
        align: 'start',
        sortable: false,
        value: 'name'
      },
      { text: 'Title', value: 'title' },
      { text: 'Type of service', value: 'type_service' },
      { text: 'Price', value: 'price' },
      { text: 'Actions', value: 'actions', sortable: false }
    ],
    services: [],
    type_serviceList: ['widescreen street banner', 'polygraphy', 'transport ads', 'media ads'],
    type_serviceSelect: null,
    editedIndex: -1,
    editedItem: {
      title: '',
      type_service: '',
      price: 0
    },
    defaultItem: {
      title: '',
      type_service: '',
      price: 0
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
    this.servicesList()
  },
  methods: {
    async servicesList () {
      try {
        const response = await axios
          .get('http://127.0.0.1:8000/luch/service/list')
        if (response.status !== 200) {
          throw new Error(response.status)
        }
        this.services = response.data
        return response.data
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    runme: function () {
      alert(this.type_serviceSelect)
    },
    editItem (item) {
      this.editedIndex = this.services.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialog = true
    },
    deleteItem (item) {
      this.editedIndex = this.services.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialogDelete = true
    },
    deleteItemConfirm () {
      if (this.editedIndex > -1) {
        this.services.splice(this.editedIndex, 1)
        this.closeDelete()
        axios.delete('http://127.0.0.1:8000/luch/service/' + JSON.stringify(this.editedItem.id), {
          id: this.editedItem.id,
          title: this.editedItem.title,
          type_service: this.editedItem.type_service,
          price: this.editedItem.price
        })
      } else {
        this.services.push(this.editedItem)
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
    save () {
      if (this.editedIndex > -1) {
        Object.assign(this.services[this.editedIndex], this.editedItem)
        axios.put('http://127.0.0.1:8000/luch/service/' + JSON.stringify(this.editedItem.id), {
          id: this.editedItem.id,
          title: this.editedItem.title,
          type_service: this.editedItem.type_service,
          price: this.editedItem.price
        })
          .then(response => {
            console.log(response)
          })
          .catch(error => {
            console.log(error)
            axios.post('http://127.0.0.1:8000/luch/service/create/', {
              title: this.editedItem.title,
              type_service: this.editedItem.type_service,
              price: this.editedItem.price
            })
          })
      }
      this.close()
    }
  }
}
</script>

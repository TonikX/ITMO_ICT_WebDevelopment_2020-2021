<template>
  <v-data-table
    :headers="headers"
    :items="chickens"
    class="elevation-1"
  >
    <template v-slot:top>
      <v-toolbar
        flat
      >
        <v-toolbar-title>Chickens</v-toolbar-title>
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
                  <v-select
                    :items="breeds"
                    v-model='editedItem.breed'
                    single-line
                    item-text='breed'
                    item-value='breed'
                    label="Breed"
                  ></v-select>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                  <v-select
                    :items="cells"
                    v-model='editedItem.cell'
                    item-text='cell'
                    item-value='cell'
                    label="Cell"
                  ></v-select>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.weight"
                      label="Weight"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.age"
                      label="Age"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.egg_amount"
                      label="Amount of eggs"
                    ></v-text-field>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                color="black"
                text
                @click="close"
              >
                Cancel
              </v-btn>
              <v-btn
                color="black"
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
        text: 'Chickens',
        align: 'start',
        sortable: false,
        value: 'name'
      },
      { text: 'Breed', value: 'breed' },
      { text: 'Cell', value: 'cell' },
      { text: 'Weight', value: 'weight' },
      { text: 'Age', value: 'age' },
      { text: 'Amount of eggs', value: 'egg_amount' },
      { text: 'Actions', value: 'actions', sortable: false }
    ],
    chickens: [],
    breeds: [],
    breedSelect: null,
    cells: [],
    editedIndex: -1,
    editedItem: {
      breed: 0,
      cell: 0,
      weight: 0,
      age: 0,
      egg_amount: 0
    },
    defaultItem: {
      breed: '',
      cell: '',
      weight: 0,
      age: 0,
      egg_amount: 0
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
    this.chickensList()
    this.breedsList()
    this.cellsList()
  },

  methods: {
    async chickensList () {
      try {
        const response = await this.axios
          .get('http://127.0.0.1:8000/birds/chickens/list')

        if (response.status !== 200) {
          throw new Error(response.status)
        }
        this.chickens = response.data
        return response.data
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    async breedsList () {
      try {
        const response = await this.axios
          .get('http://127.0.0.1:8000/birds/breeds/list')

        if (response.status !== 200) {
          throw new Error(response.status)
        }
        this.breeds = response.data
        return response.data
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    async cellsList () {
      try {
        const response = await this.axios
          .get('http://127.0.0.1:8000/birds/cells/list')

        if (response.status !== 200) {
          throw new Error(response.status)
        }
        this.cells = response.data
        return response.data
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },

    editItem (item) {
      this.editedIndex = this.chickens.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialog = true
    },

    deleteItem (item) {
      this.editedIndex = this.chickens.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialogDelete = true
    },

    deleteItemConfirm () {
      if (this.editedIndex > -1) {
        this.chickens.splice(this.editedIndex, 1)
        this.closeDelete()
        axios.delete('http://127.0.0.1:8000/birds/chickens/info/' + JSON.stringify(this.editedItem.id), {
          id: this.editedItem.id,
          breed: this.editedItem.breed,
          cell: this.editedItem.cell,
          weight: this.editedItem.weight,
          age: this.editedItem.age,
          egg_amount: this.editedItem.egg_amount
        })
      } else {
        this.chickens.push(this.editedItem)
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
      console.log('Entered save')
      if (this.editedIndex > -1) {
        Object.assign(this.chickens[this.editedIndex], this.editedItem)
        axios.put('http://127.0.0.1:8000/birds/chickens/info/' + JSON.stringify(this.editedItem.id), {
          weight: this.editedItem.weight,
          age: this.editedItem.age,
          egg_amount: this.editedItem.egg_amount
        })
      } else {
        axios.post('http://127.0.0.1:8000/birds/chickens/create/', {
          breed: this.editedItem.breed,
          cell: this.editedItem.cell,
          weight: this.editedItem.weight,
          age: this.editedItem.age,
          egg_amount: this.editedItem.egg_amount
        })
      }
      this.close()
    }
  }
}
</script>

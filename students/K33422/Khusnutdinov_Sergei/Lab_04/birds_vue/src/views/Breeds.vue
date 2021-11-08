<template>
  <v-data-table
    :headers="headers"
    :items="breeds"
    class="elevation-1"
  >
    <template v-slot:top>
      <v-toolbar
        flat
      >
        <v-toolbar-title>Breeds</v-toolbar-title>
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
                      v-model="editedItem.breed"
                      label="Breed"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                  <v-select
                    :items="productivityList"
                    v-model='editedItem.productivity'
                    single-line
                    item-text='productivity'
                    item-value='productivity'
                    label="Productivity"
                  ></v-select>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.avg_weight"
                      label="Average weight"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.diet"
                      label="Diet"
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
    dialog: false,
    dialogDelete: false,
    headers: [
      {
        text: 'Breeds',
        align: 'start',
        sortable: false,
        value: 'name'
      },
      { text: 'Breed', value: 'breed' },
      { text: 'Productivity', value: 'productivity' },
      { text: 'Average weight', value: 'avg_weight' },
      { text: 'Diet', value: 'diet' },
      { text: 'Actions', value: 'actions', sortable: false }
    ],
    breeds: [],
    productivityList: ['low', 'avg', 'high'],
    productivitySelect: null,
    editedIndex: -1,
    editedItem: {
      breed: '',
      productivity: '',
      avg_weight: 0,
      diet: ''
    },
    defaultItem: {
      breed: '',
      productivity: '',
      avg_weight: 0,
      diet: ''
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
    this.breedsList()
  },
  methods: {
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
    runme: function () {
      alert(this.productivitySelect)
    },
    editItem (item) {
      this.editedIndex = this.breeds.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialog = true
    },
    deleteItem (item) {
      this.editedIndex = this.breeds.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialogDelete = true
    },
    deleteItemConfirm () {
      if (this.editedIndex > -1) {
        this.breeds.splice(this.editedIndex, 1)
        this.closeDelete()
        axios.delete('http://127.0.0.1:8000/birds/breeds/info/' + JSON.stringify(this.editedItem.id), {
          id: this.editedItem.id,
          breed: this.editedItem.breed,
          productivity: this.editedItem.productivity,
          avg_weight: this.editedItem.avg_weight,
          diet: this.editedItem.diet
        })
      } else {
        this.breeds.push(this.editedItem)
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
        Object.assign(this.breeds[this.editedIndex], this.editedItem)
        axios.put('http://127.0.0.1:8000/birds/breeds/info/' + JSON.stringify(this.editedItem.id), {
          id: this.editedItem.id,
          breed: this.editedItem.breed,
          productivity: this.editedItem.productivity,
          avg_weight: this.editedItem.avg_weight,
          diet: this.editedItem.diet
        })
      } else {
        axios.post('http://127.0.0.1:8000/birds/breeds/create/', {
          breed: this.editedItem.breed,
          productivity: this.editedItem.productivity,
          avg_weight: this.editedItem.avg_weight,
          diet: this.editedItem.diet
        })
      }
      this.close()
    }
  }
}
</script>

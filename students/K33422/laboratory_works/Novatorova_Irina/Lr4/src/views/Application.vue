<template>
  <v-data-table
    :headers="headers"
    :items="applications"
    class="elevation-2"
  >
    <template v-slot:top>
      <v-toolbar
        flat
      >
        <v-toolbar-title>Applications</v-toolbar-title>
        <v-divider
          class="mx-5"
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
                      v-model="editedItem.client"
                      label="Client"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.service"
                      label="Service"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.date"
                      label="Date"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.ad_product"
                      label="Ad product"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.amount"
                      label="Amount"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                  <v-select
                    :items="statusList"
                    v-model='editedItem.status'
                    single-line
                    item-text='status'
                    item-value='status'
                    label="Status"
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
        text: 'Application',
        align: 'start',
        sortable: false,
        value: 'name'
      },
      { text: 'Client', value: 'client' },
      { text: 'Service', value: 'service' },
      { text: 'Date', value: 'date' },
      { text: 'Ad product', value: 'ad_product' },
      { text: 'Amount', value: 'amount' },
      { text: 'Status', value: 'status' },
      { text: 'Actions', value: 'actions', sortable: false }
    ],
    applications: [],
    statusList: ['payed', 'not payed'],
    statusSelect: null,
    editedIndex: -1,
    editedItem: {
      client: '',
      service: '',
      date: '',
      ad_product: '',
      amount: '',
      status: ''
    },
    defaultItem: {
      client: '',
      service: '',
      date: '',
      ad_product: '',
      amount: '',
      status: ''
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
    this.applicationsList()
  },
  methods: {
    async applicationsList () {
      try {
        const response = await axios
          .get('http://127.0.0.1:8000/luch/application/list')
        if (response.status !== 200) {
          throw new Error(response.status)
        }
        this.applications = response.data
        return response.data
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    runme: function () {
      alert(this.statusSelect)
    },
    editItem (item) {
      this.editedIndex = this.applications.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialog = true
    },
    deleteItem (item) {
      this.editedIndex = this.applications.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialogDelete = true
    },
    deleteItemConfirm () {
      if (this.editedIndex > -1) {
        this.applications.splice(this.editedIndex, 1)
        this.closeDelete()
        axios.delete('http://127.0.0.1:8000/luch/application/' + JSON.stringify(this.editedItem.id), {
          id: this.editedItem.id,
          breed: this.editedItem.breed,
          productivity: this.editedItem.productivity,
          avg_weight: this.editedItem.avg_weight,
          diet: this.editedItem.diet
        })
      } else {
        this.applications.push(this.editedItem)
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
        Object.assign(this.breeds[this.editedIndex], this.editedItem)
        axios.put('http://127.0.0.1:8000/luch/application/' + JSON.stringify(this.editedItem.id), {
          id: this.editedItem.id,
          breed: this.editedItem.breed,
          productivity: this.editedItem.productivity,
          avg_weight: this.editedItem.avg_weight,
          diet: this.editedItem.diet
        })
          .then(response => {
            console.log(response)
          })
          .catch(error => {
            console.log(error)
            axios.post('http://127.0.0.1:8000/luch/application/create/', {
              application: this.editedItem.breed,
              productivity: this.editedItem.productivity,
              avg_weight: this.editedItem.avg_weight,
              diet: this.editedItem.diet
            })
          })
      }
      this.close()
    }
  }
}
</script>

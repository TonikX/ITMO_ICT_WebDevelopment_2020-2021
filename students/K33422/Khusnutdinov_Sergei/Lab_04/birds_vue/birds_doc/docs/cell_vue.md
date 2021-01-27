# Cell vue

Allows to see all cells, edit, add, delete them.

**URL** : `/cellslist/`

**Methods** : `GET`, `PUT`, `POST`, `DELETE`

Success Responses

**Code** : `200 OK`, `201 Created`

**Methods** :

```javascript
<script>
import axios from 'axios'
export default {
  data: () => ({
    dialog: false,
    dialogDelete: false,
    flag: false,
    headers: [
      {
        text: 'Cells',
        align: 'start',
        sortable: false,
        value: 'name'
      },
      { text: 'Cell', value: 'cell' },
      { text: 'Row', value: 'row' },
      { text: 'Tsekh', value: 'tsekh' },
      { text: 'Actions', value: 'actions', sortable: false }
    ],
    cells: [],
    editedIndex: -1,
    editedItem: {
      cell: 0,
      row: 0,
      tsekh: 0
    },
    defaultItem: {
      cell: 0,
      row: 0,
      tsekh: 0
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
    this.cellsList()
  },

  methods: {
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
      this.editedIndex = this.cells.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialog = true
    },

    deleteItem (item) {
      this.editedIndex = this.cells.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialogDelete = true
    },

    deleteItemConfirm () {
      if (this.editedIndex > -1) {
        this.cells.splice(this.editedIndex, 1)
        this.closeDelete()
        axios.delete('http://127.0.0.1:8000/birds/cells/info/' + JSON.stringify(this.editedItem.id), {
          id: this.editedItem.id,
          cell: this.editedItem.cell,
          row: this.editedItem.row,
          tsekh: this.editedItem.tsekh
        })
      } else {
        this.cells.push(this.editedItem)
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
        Object.assign(this.cells[this.editedIndex], this.editedItem)
        axios.put('http://127.0.0.1:8000/birds/cells/info/' + JSON.stringify(this.editedItem.id), {
          id: this.editedItem.id,
          cell: this.editedItem.cell,
          row: this.editedItem.row,
          tsekh: this.editedItem.tsekh
        })
      } else {
        axios.post('http://127.0.0.1:8000/birds/cells/create/', {
          cell: this.editedItem.cell,
          row: this.editedItem.row,
          tsekh: this.editedItem.tsekh
        })
      }
      this.close()
    }
  }
}
</script>
```
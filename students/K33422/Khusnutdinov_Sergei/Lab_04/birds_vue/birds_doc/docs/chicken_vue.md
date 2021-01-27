# Chicken vue

Allows to see chicken, add, delete, edit them.

**URL** : `/chickenslist/`

**Methods** : `GET`, `PUT`, `POST`, `DELETE`

Success Responses

**Code** : `200 OK`, `201 Created`

**Methods** :

```javascript
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
```
# Breed vue

Allow to see all breeds, edit, delete, add them.

**URL** : `/breedslist/`

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
```
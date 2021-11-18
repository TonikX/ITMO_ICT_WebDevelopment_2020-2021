# Cell's table + options

Выводит информацию обо всех клетках в системе и позволяет добавлять, редактировать и удалять данные

**URL** : `/cellslist/`

**Methods** : `GET`, `PUT`, `POST`, `DELETE`

## Success Responses

**Code** : `200 OK`, `201 Created`

**Methods** :

```javascript
async cellsList () {
      try {
        const response = await this.axios
          .get('http://127.0.0.1:8000/poultry/cells/list')

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

    save () {
      if (this.editedIndex > -1) {
        Object.assign(this.cells[this.editedIndex], this.editedItem)
        axios.put('http://127.0.0.1:8000/poultry/cells/info/' + JSON.stringify(this.editedItem.id), {
          id: this.editedItem.id,
          cell: this.editedItem.cell,
          row: this.editedItem.row,
          tsekh: this.editedItem.tsekh
        })
          .then(response => {
            console.log(response)
          })
```
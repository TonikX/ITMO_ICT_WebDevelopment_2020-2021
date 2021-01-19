# Chicken's table + options

Выводит информацию обо всех курицах в системе и позволяет добавлять, редактировать и удалять данные

**URL** : `/chickenslist/`

**Methods** : `GET`, `PUT`, `POST`, `DELETE`

## Success Responses

**Code** : `200 OK`, `201 Created`

**Methods** :

```javascript
async chickensList () {
      try {
        const response = await this.axios
          .get('http://127.0.0.1:8000/poultry/chickens/list')

        if (response.status !== 200) {
          throw new Error(response.status)
        }
        this.chickens = response.data
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

    save () {
      if (this.editedIndex > -1) {
        Object.assign(this.chickens[this.editedIndex], this.editedItem)
        axios.put('http://127.0.0.1:8000/poultry/chickens/info/' + JSON.stringify(this.editedItem.id), {
          id: this.editedItem.id,
          breed: this.editedItem.breed,
          cell: this.editedItem.cell,
          weight: this.editedItem.weight,
          age: this.editedItem.age,
          egg_amount: this.editedItem.egg_amount
        })
          .then(response => {
            console.log(response)
          })
```
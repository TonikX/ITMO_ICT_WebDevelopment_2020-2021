# Breed's table + options

Выводит информацию обо всех породах в системе и позволяет добавлять, редактировать и удалять данные

**URL** : `/breedslist/`

**Methods** : `GET`, `PUT`, `POST`, `DELETE`

## Success Responses

**Code** : `200 OK`, `201 Created`

**Methods** :

```javascript
async breedsList () {
      try {
        const response = await this.axios
          .get('http://127.0.0.1:8000/poultry/breeds/list')

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

    save () {
      if (this.editedIndex > -1) {
        Object.assign(this.breeds[this.editedIndex], this.editedItem)
        axios.put('http://127.0.0.1:8000/poultry/breeds/info/' + JSON.stringify(this.editedItem.id), {
          id: this.editedItem.id,
          breed: this.editedItem.breed,
          productivity: this.editedItem.productivity,
          avg_weight: this.editedItem.avg_weight,
          diet: this.editedItem.diet
        })
          .then(response => {
            console.log(response)
          })
```
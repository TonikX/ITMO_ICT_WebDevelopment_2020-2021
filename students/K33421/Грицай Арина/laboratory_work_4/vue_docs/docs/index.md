# Home.vue - Authorization

**URL** : `/auth/token/login/`

**Methods** : `POST`

## Success Responses

**Code** : `200 OK`

**Content** : `{}`

```javascript
async signIn () 
    {
      try {
        const response = await this.axios
          .post('http://127.0.0.1:8000/auth/token/login/', this.signInForm)
        console.log('SIGN IN RESPONSE', response)
        this.$refs.signInForm.reset()
        localStorage.setItem('token', response.data.auth_token)

        this.$router.push('/profile')
        this.$router.go()
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    }
```

# SignUp.vue - Create a new user

**URL** : `/auth/users/`

**Methods** : `POST`

## Success Responses

**Code** : `201 Created`

**Content** : `{}`

```javascript
async signIn () 
    {
      try {
        const response = await this.axios
          .post('http://127.0.0.1:8000/auth/token/login/', this.signInForm)
        console.log('SIGN IN RESPONSE', response)
          
        this.$refs.signInForm.reset()
        localStorage.setItem('token', response.data.auth_token)

        this.$router.push('/profile')
        this.$router.go()
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    }
```

# Profile.vue - User's profile (could be edited by authorized user)

**URL** : `/profile/`

**Methods** : `GET`, `PATCH`

## Success Responses

**Code** : `200 OK`

**Content** : `{}`

```json
    {
        "first_name": "Ully",
        "last_name": "Rain",
        "passport": "6666 1234567"
    }
```

# Cells.vue

Displays information about all cells in the system and allows you to add, edit and delete data.

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
    deleteItemConfirm () {
      if (this.editedIndex > -1) {
        this.cells.splice(this.editedIndex, 1)
        this.closeDelete()
        axios.delete('http://127.0.0.1:8000/poultry/cells/info/' + JSON.stringify(this.editedItem.id), {
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
          .catch(error => {
            console.log(error)
            axios.post('http://127.0.0.1:8000/poultry/cells/add/', {
              cell: this.editedItem.cell,
              row: this.editedItem.row,
              tsekh: this.editedItem.tsekh
            })
          })
      }
    }
```

# Breeds.vue 

Displays information about all breeds in the system and allows you to add, edit and delete data.

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
    deleteItemConfirm () {
      if (this.editedIndex > -1) {
        this.breeds.splice(this.editedIndex, 1)
        this.closeDelete()
        axios.delete('http://127.0.0.1:8000/poultry/breeds/info/' + JSON.stringify(this.editedItem.id), {
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
          .catch(error => {
            console.log(error)
            axios.post('http://127.0.0.1:8000/poultry/breeds/add/', {
              breed: this.editedItem.breed,
              productivity: this.editedItem.productivity,
              avg_weight: this.editedItem.avg_weight,
              diet: this.editedItem.diet
            })
          })
      }
      this.close()
    }
```
# Chickens.vue 

Displays information about all chickens in the system and allows you to add, edit and delete data.

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
        axios.delete('http://127.0.0.1:8000/poultry/chickens/info/' + JSON.stringify(this.editedItem.id), {
          id: this.editedItem.id,
          breed: this.editedItem.breed,
          cell: this.editedItem.cell,
          weight: this.editedItem.weight,
          age: this.editedItem.age,
          egg_quantity: this.editedItem.egg_quantity
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
      if (this.editedIndex > -1) {
        Object.assign(this.chickens[this.editedIndex], this.editedItem)
        axios.put('http://127.0.0.1:8000/poultry/chickens/info/' + JSON.stringify(this.editedItem.id), {
          id: this.editedItem.id,
          breed: this.editedItem.breed,
          cell: this.editedItem.cell,
          weight: this.editedItem.weight,
          age: this.editedItem.age,
          egg_quantity: this.editedItem.egg_quantity
        })
          .then(response => {
            console.log(response)
          })
          .catch(error => {
            console.log(error)
            console.log(this.editedItem.breed)
            console.log(this.editedItem.cell)
            axios.post('http://127.0.0.1:8000/poultry/chickens/add/', {
              weight: this.editedItem.weight,
              age: this.editedItem.age,
              egg_quantity: this.editedItem.egg_quantity,
              breed: this.editedItem.breed,
              cell: this.editedItem.cell
            })
          })
      }
      this.close()
    }
```

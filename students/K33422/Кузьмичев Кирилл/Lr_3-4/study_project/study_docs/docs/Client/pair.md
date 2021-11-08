## Pair 

###Create 

Создать пару

**URL** : `/pair/create/`

**Methods** : `POST`

#### Success Responses

**Code** : `201 Created`

**Content** : `{}`

```javascript
    async add () {
      await this.axios
        .post('http://127.0.0.1:8000/pair/create/', this.addForm)
        .then((res) => {
          console.log(res)
          this.$refs.addForm.reset()
        })
        .catch((error) => {
          console.log(error)
        })
    }
}
```

### List

Просмотреть данные о парах

**URL** : `/pair/list/`

**Methods** : `GET`

#### Success Responses

**Code** : `200 OK`

**Content** : `[{}]`

```javascript
    await this.axios
      .get('http://127.0.0.1:8000/pair/list/')
      .then((res) => {
        console.log('this.pairs', this.pairs)
        this.pairs = res.data
      })
      .catch((error) => {
        console.log(error)
      })
}
```

### Edit 

Удалить / изменить пару

**URL** : `/pair/:pair_id/`

**Methods** : `PUT / DELETE`

#### Success Responses

**Code** : `200 OK / 204 No Content`

**Content** : `{}`

```javascript
    async update () {
      await this.axios
        .put(`http://127.0.0.1:8000/pair/${this.st_id}/`, this.addForm)
        .then((res) => {
          console.log(res)
          this.$refs.addForm.reset()
          this.$router.go(0)
        })
        .catch((error) => {
          console.log(error)
        })
    }
    
    async deleteElem (elem) {
      await this.axios
        .delete(`http://127.0.0.1:8000/pair/${elem}`)
        .then((res) => {
          console.log(res)
          this.$router.go(0)
        })
        .catch((error) => {
          console.log(error)
        })
    }
}
```
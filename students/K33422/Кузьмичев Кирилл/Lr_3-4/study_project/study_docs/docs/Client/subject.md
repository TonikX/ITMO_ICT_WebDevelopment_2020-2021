## Subject

###Create 

Создать предмет

**URL** : `/subject/create/`

**Methods** : `POST`

#### Success Responses

**Code** : `201 Created`

**Content** : `{}`

```javascript
    async add () {
      await this.axios
        .post('http://127.0.0.1:8000/subject/create/', this.addForm)
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

Просмотреть данные о предмете 

**URL** : `/subject/list/`

**Methods** : `GET`

#### Success Responses

**Code** : `200 OK`

**Content** : `[{}]`

```javascript
    await this.axios
      .get('http://127.0.0.1:8000/subject/list/')
      .then((res) => {
        console.log('this.subjects', this.subjects)
        this.subjects = res.data
      })
      .catch((error) => {
        console.log(error)
      })
}
```

### Edit 

Удалить / изменить предмет

**URL** : `/subject/:subject_id/`

**Methods** : `PUT / DELETE`

#### Success Responses

**Code** : `200 OK / 204 No Content`

**Content** : `{}`

```javascript
    async update () {
      await this.axios
        .put(`http://127.0.0.1:8000/subject/${this.st_id}/`, this.addForm)
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
        .delete(`http://127.0.0.1:8000/subject/${elem}`)
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
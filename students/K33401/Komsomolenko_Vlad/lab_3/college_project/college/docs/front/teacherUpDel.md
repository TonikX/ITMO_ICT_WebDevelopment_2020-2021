# Teacher Edit 

Изменить информацию о преподавателе или удалить преподавателя

**URL** : `/updateteacher/:teacher_id/`

**Methods** : `PUT / DELETE`

## Success Responses

**Code** : `200 OK / 204 No Content`

**Content** : `{}`

```javascript
    async delTr (tr) {
      await this.axios
        .delete(`http://127.0.0.1:8000/college/teacher/updel/${tr}`)
        .then((res) => {
          console.log(res)
          this.$router.go()
        })
        .catch((error) => {
          console.log(error)
        })
    }
    async update () {
      await this.axios
        .put(`http://127.0.0.1:8000/college/teacher/updel/${this.tr_id}`, this.newTr)
        .then((res) => {
          console.log(res)
          window.location.href = '/teachers'
        })
        .catch((error) => {
          console.log(error)
        })
    }
```
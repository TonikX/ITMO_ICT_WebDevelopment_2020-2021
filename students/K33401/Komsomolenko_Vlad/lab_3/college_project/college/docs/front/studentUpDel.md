# Student Edit 

Изменить информацию о студенте или удалить студента

**URL** : `/updatestudent/:student_id/`

**Methods** : `PUT / DELETE`

## Success Responses

**Code** : `200 OK / 204 No Content`

**Content** : `{}`

```javascript
    async update () {
      await this.axios
        .put(`http://127.0.0.1:8000/college/student/updel/${this.st_id}`, this.newSt)
        .then((res) => {
          console.log(res)
          window.location.href = '/students'
        })
        .catch((error) => {
          console.log(error)
        })
    }
  }
    async delSt (st) {
      await this.axios
        .delete(`http://127.0.0.1:8000/college/student/updel/${st}`)
        .then((res) => {
          this.$router.go()
        })
        .catch((error) => {
          console.log(error)
        })
    }
```
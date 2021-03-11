# Room Edit 

Удалить / изменить номер

**URL** : `/mark/:mark_id/`

**Methods** : `PUT / DELETE`

## Success Responses

**Code** : `200 OK / 204 No Content`

**Content** : `{}`

```javascript
    async update () {
      await this.axios
        .put(`http://127.0.0.1:8000/room/${this.cur_id}/`, this.addForm)
        .then((res) => {
          console.log(res)
        })
        .catch((error) => {
          console.log(error)
          alert('Введены некоректные данные!')
        })
      this.$refs.addForm.reset()
      window.location.href = `http://localhost:8080/room/${this.cur_id}`
    }
    
    async deleteElem (el) {
      await this.axios
        .delete(`http://127.0.0.1:8000/room/${el}`)
        .then((res) => {
          console.log(res)
          this.$router.go()
        })
        .catch((error) => {
          console.log(error)
        })
    }
}
```
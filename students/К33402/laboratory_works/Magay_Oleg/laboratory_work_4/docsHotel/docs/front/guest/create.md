# Guest create

Заселение гостя и обновление статуса соответсвующего номера

**URL** : `/guest/create`

**Methods** : `POST`

## Success Responses

**Code** : `201 Created`

**Content** : `{}`

```javascript
    async add () {
      await this.axios
        .post('http://127.0.0.1:8000/guest/create/', this.addForm)
        .then((res) => {
          console.log(res)
        })
        .catch((error) => {
          console.log(error)
        })
      await this.axios
        .get(`http://127.0.0.1:8000/room/${this.addForm.room}/`)
        .then((res) => {
          console.log(res.data)
          this.next_room = res.data
        })
        .catch((error) => {
          console.log(error)
        })
      this.next_room.status = 'busy'
      await this.axios
        .put(`http://127.0.0.1:8000/room/${this.addForm.room}/`, this.next_room)
        .then((res) => {
          console.log(res.data)
        })
        .catch((error) => {
          console.log(error)
        })
      this.$refs.addForm.reset()
    }
}
```
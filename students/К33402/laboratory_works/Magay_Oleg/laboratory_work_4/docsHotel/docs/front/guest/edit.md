# Guest detail

Обновление / удаление данных о госте.

При выселении гостя статус номера сменяется на "свободно" и увеличивается прибыль с него. При смене номера меняются также их статусы.

**URL** : `/guest/:guest_id`

**Methods** : `PUT, DELETE`

## Success Responses

**Code** : `200 OK, 204 No Conent`

**Content** : `{}`

```javascript
    async update () {
      await this.axios
        .put(`http://127.0.0.1:8000/guest/${this.cur_id}/`, this.addForm)
        .then((res) => {
          console.log(res)
        })
        .catch((error) => {
          console.log(error)
          alert('Введены некоректные данные!')
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
      this.room.status = 'free'
      await this.axios
        .put(`http://127.0.0.1:8000/room/${this.cur.room}/`, this.room)
        .then((res) => {
          console.log(res.data)
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
      console.log('this.room', this.room, 'next', this.next_room)
      this.$refs.addForm.reset()
      window.location.href = `http://localhost:8080/guest/${this.cur_id}`
    }
    
    async deleteElem (id, room) {
      await this.axios
        .delete(`http://127.0.0.1:8000/guest/${id}`)
        .then((res) => {
          console.log(res)
        })
        .catch((error) => {
          console.log(error)
        })
      await this.axios
        .get(`http://127.0.0.1:8000/room/${room}`)
        .then((res) => {
          this.room = res.data
          console.log('this.room', this.room)
        })
      this.room.total = this.room.total + this.room.price
      this.room.status = 'free'
      await this.axios
        .put(`http://127.0.0.1:8000/room/${room}/`, this.room)
        .then((res) => {
          console.log(res.data)
        })
        .catch((error) => {
          console.log(error)
        })
    }
    
}
```
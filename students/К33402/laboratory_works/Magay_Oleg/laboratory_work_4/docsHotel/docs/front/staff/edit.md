# Staff Edit 

Уволить первонал или изменить данные

**URL** : `/staff/:staff_id/`

**Methods** : `PUT / DELETE`

## Success Responses

**Code** : `200 OK / 204 No Content`

**Content** : `{}`

```javascript
    async update () {
      await this.axios
        .put(`http://127.0.0.1:8000/staff/${this.cur_id}/`, this.addForm)
        .then((res) => {
          console.log(res)
        })
        .catch((error) => {
          console.log(error)
          alert('Введены некоректные данные!')
        })
      for (const param of this.cur.cleaning) {
        const id = await this.axios
          .get('http://127.0.0.1:8000/staff_cleaning/list/')
          .then((res) => {
            console.log(res.data)
            return res.data.filter(val => val.staff.toString() === this.cur_id && val.params === param.id)[0].id
          })
          .catch((error) => {
            console.log(error)
          })
        await this.axios
          .delete(`http://127.0.0.1:8000/staff_cleaning/${id}/`)
          .then((res) => {
            console.log(res)
          })
          .catch((error) => {
            console.log(error)
          })
      }
      for (const param of this.addParams.params) {
        await this.axios
          .post('http://127.0.0.1:8000/staff_cleaning/create/', {
            staff: this.cur_id,
            params: param
          })
          .then((res) => {
            console.log(res)
          })
          .catch((error) => {
            console.log(error)
          })
      }
      window.location.href = `http://localhost:8080/staff/${this.cur_id}`
    }
    
    async deleteElem (el) {
      await this.axios
        .delete(`http://127.0.0.1:8000/staff/${el}`)
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
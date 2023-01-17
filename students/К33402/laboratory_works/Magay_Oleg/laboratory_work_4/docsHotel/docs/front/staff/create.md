# Staff Create 

Нанять персонал

**URL** : `/staff/create/`

**Methods** : `POST`

## Success Responses

**Code** : `201 Created`

**Content** : `{}`

```javascript
    async add () {
      await this.axios
        .post('http://127.0.0.1:8000/staff/create/', this.addForm)
        .then((res) => {
          console.log(res)
        })
        .catch((error) => {
          console.log(error)
        })
      await this.axios
        .get('http://127.0.0.1:8000/staff/list/')
        .then((res) => {
          this.staff_id = res.data[res.data.length - 1].id
        })
        .catch((error) => {
          console.log(error)
        })
      for (const param of this.addParams.params) {
        await this.axios
          .post('http://127.0.0.1:8000/staff_cleaning/create/', {
            staff: this.staff_id,
            params: param
          })
          .then((res) => {
            console.log(res)
          })
          .catch((error) => {
            console.log(error)
          })
      }
      this.$refs.addForm.reset()
    }
}
```
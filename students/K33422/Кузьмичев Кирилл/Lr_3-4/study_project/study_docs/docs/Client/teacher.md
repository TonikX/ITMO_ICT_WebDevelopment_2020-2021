## Teacher

###Create 

Создать преподавателя и его предметы

**URL** : `/teacher/create/`

**Methods** : `POST`

#### Success Responses

**Code** : `201 Created`

**Content** : `{}`

```javascript
    async add () {
      await this.axios
        .post('http://127.0.0.1:8000/teacher/create/', this.addForm)
        .then((res) => {
          console.log(res)
        })
        .catch((error) => {
          console.log(error)
        })
      await this.axios
        .get('http://127.0.0.1:8000/teacher/list/')
        .then((res) => {
          this.teacher_id = res.data[res.data.length - 1].id
        })
        .catch((error) => {
          console.log(error)
        })
      for (const sub of this.addSub.subject) {
        await this.axios
          .post('http://127.0.0.1:8000/subteach/create/', {
            teacher: this.teacher_id,
            subject: sub
          })
          .then((res) => {
            console.log(res)
            this.$refs.reset()
          })
          .catch((error) => {
            console.log(error)
          })
      }
    }
}
```

### List

Просмотреть данные о преподавателе и его предметах

**URL** : `/teacher/list/`

**Methods** : `GET`

#### Success Responses

**Code** : `200 OK`

**Content** : `[{}]`

```javascript
    await this.axios
      .get('http://127.0.0.1:8000/teacher/list/')
      .then((res) => {
        console.log('this.teachers', this.teachers)
        this.teachers = res.data
      })
      .catch((error) => {
        console.log(error)
      })
}
```

### Edit 

Удалить / изменить преподавателя и его предметы

**URL** : `/teacher/:teacher_id/`

**Methods** : `PUT / DELETE`

#### Success Responses

**Code** : `200 OK / 204 No Content`

**Content** : `{}`

```javascript
    async update () {
      await this.axios
        .put(`http://127.0.0.1:8000/teacher/${this.t_id}/`, this.addForm)
        .then((res) => {
          console.log(res)
        })
        .catch((error) => {
          console.log(error)
        })
      for (const sub of this.t_cur.subjects) {
        const id = await this.axios
          .get('http://127.0.0.1:8000/subteach/list/')
          .then((res) => {
            console.log(res.data)
            return res.data.filter(val => val.teacher.toString() === this.t_id && val.subject === sub.id)[0].id
          })
          .catch((error) => {
            console.log(error)
          })
        await this.axios
          .delete(`http://127.0.0.1:8000/subteach/${id}/`)
          .then((res) => {
            console.log(res)
          })
          .catch((error) => {
            console.log(error)
          })
      }
      for (const sub of this.addSub.subject) {
        await this.axios
          .post('http://127.0.0.1:8000/subteach/create/', {
            teacher: this.t_id,
            subject: sub
          })
          .then((res) => {
            console.log(res)
          })
          .catch((error) => {
            console.log(error)
          })
      }
      this.$refs.addForm.reset()
      this.$router.go(0)
    }
}
```
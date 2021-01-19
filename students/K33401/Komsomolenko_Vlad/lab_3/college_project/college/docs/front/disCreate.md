# Discipline Create 

Создание дисциплины

**URL** : `/creatediscipline`

**Methods** : `POST`

## Success Responses

**Code** : `201 Created`

**Content** : `{}`

```javascript
    async addDiscipline () {
      await this.axios
        .post('http://127.0.0.1:8000/college/discipline/create/', this.discipline)
        .then((res) => {
          console.log(res)
          window.location.href = ''
        })
        .catch((error) => {
          console.log(error)
        })
    },

    async addDiscTeacher () {
      await this.axios
        .post('http://127.0.0.1:8000/college/teacher/adddisc/', this.discTeacher)
        .then((res) => {
          console.log(res)
          window.location.href = ''
        })
        .catch((error) => {
          console.log(error)
        })
    }
```
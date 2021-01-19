# Teacher Create

Создание преподавателя

**URL** : `/createteacher`

**Methods** : `POST`

## Success Responses

**Code** : `201 Created`

**Content** : `{}`

```javascript
    async addTeacher () {
      await this.axios
        .post('http://127.0.0.1:8000/college/teacher/create/', this.teacher)
        .then((res) => {
          console.log(res)
          window.location.href = '/teachers'
        })
        .catch((error) => {
          console.log(error)
        })
    }
```
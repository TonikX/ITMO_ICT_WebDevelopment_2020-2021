# Student Create 

Создание студента

**URL** : `/createstudent`

**Methods** : `POST`

## Success Responses

**Code** : `201 Created`

**Content** : `{}`

```javascript
    async addStudent () {
      await this.axios
        .post('http://127.0.0.1:8000/college/student/create/', this.student)
        .then((res) => {
          console.log(res)
          window.location.href = '/students'
        })
        .catch((error) => {
          console.log(error)
        })
    }
```
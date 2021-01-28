# Students List

Список всех студентов

**URL** : `/students`

**Methods** : `GET`

## Success Responses

**Code** : `200 OK`

**Content** : `[{}]`

```javascript
    this.axios
      .get('http://127.0.0.1:8000/college/students/')
      .then((res) => {
        this.students = res.data
      })
      .catch((error) => {
        console.log(error)
      })
```_
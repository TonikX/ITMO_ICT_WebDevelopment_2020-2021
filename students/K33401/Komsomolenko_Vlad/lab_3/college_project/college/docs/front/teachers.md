# Teachers List

Список всех преподавателей

**URL** : `/teachers`

**Methods** : `GET`

## Success Responses

**Code** : `200 OK`

**Content** : `[{}]`

```javascript
    await this.axios
      .get('http://127.0.0.1:8000/college/teachers/')
      .then((res) => {
        this.teachers = res.data
      })
      .catch((error) => {
        console.log(error)
      })
    await this.axios
      .get('http://127.0.0.1:8000/college/disciplines/')
      .then((res) => {
        this.disciplines = res.data
        for (const teacher of this.teachers) {
          const names = []
          for (const dis of teacher.discipline) {
            const nameId = dis - 1
            names.push(this.disciplines[nameId].title)
          }
          teacher.discipline = names
        }
      })
```
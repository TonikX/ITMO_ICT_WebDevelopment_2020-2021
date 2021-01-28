# Pair Create 

Создание новой пары

**URL** : `/createpair`

**Methods** : `POST`

## Success Responses

**Code** : `201 Created`

**Content** : `{}`

```javascript

    await this.axios
      .get('http://127.0.0.1:8000/college/teachers')
      .then((res) => {
        this.teachers = res.data
      })
      .catch((error) => {
        console.log(error)
      })
    await this.axios
      .get('http://127.0.0.1:8000/college/disciplines')
      .then((res) => {
        for (const dis of res.data) {
          for (const teacher of this.teachers) {
            if (teacher.discipline.includes(dis.id)) {
              this.disciplines.push(dis)
              break
            }
          }
        }
      })
      .catch((error) => {
        console.log(error)
      })
    async addPair () {
      console.log(this.pair)
      await this.axios
        .post('http://127.0.0.1:8000/college/pair/create/', this.pair)
        .then((res) => {
          window.location.href = '/pairs'
          console.log(res)
        })
        .catch((error) => {
          console.log(error)
        })
    }
```
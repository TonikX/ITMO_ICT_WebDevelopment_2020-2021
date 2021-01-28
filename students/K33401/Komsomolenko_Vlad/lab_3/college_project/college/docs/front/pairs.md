# Pairs List

Список всех пар

**URL** : `/pairs`

**Methods** : `GET`

## Success Responses

**Code** : `200 OK`

**Content** : `[{}]`

```javascript

    this.axios
      .get('http://127.0.0.1:8000/college/pairs/')
      .then((res) => {
        this.pairs = res.data
      })
      .catch((error) => {
        console.log(error)
      })
    this.axios
      .get('http://127.0.0.1:8000/college/disciplines/')
      .then((res) => {
        this.disciplines = res.data
        for (const pair of this.pairs) {
          const p = {
            day: '',
            time: '',
            group: '',
            discipline: ''
          }
          p.day = pair.day
          p.time = pair.time
          p.group = pair.group
          p.discipline = this.disciplines[pair.discipline].title
          this.allPairs.push(p)
        }
      })
      .catch((error) => {
        console.log(error)
      })
```
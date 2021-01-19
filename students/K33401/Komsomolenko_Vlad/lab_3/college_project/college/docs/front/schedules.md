# Schedules List

Список всех расписаний

**URL** : `/schedules`

**Methods** : `GET`

## Success Responses

**Code** : `200 OK`

**Content** : `[{}]`

```javascript

    this.axios
      .get('http://127.0.0.1:8000/college/schedules/')
      .then((res) => {
        this.schedules = res.data
      })
      .catch((error) => {
        console.log(error)
      })
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
        for (const schedule of this.schedules) {
          console.log(schedule)
          const s = {
            group: '',
            pair: []
          }
          s.group = schedule.group
          for (const pair of schedule.pair) {
            const p = {
              day: '0',
              time: '',
              discipline: ''
            }
            for (const curPair of this.pairs) {
              if (curPair.id === pair) {
                p.day = curPair.day
                p.time = curPair.time
                const idDisc = curPair.discipline - 1
                p.discipline = this.disciplines[idDisc].title
              }
            }
            s.pair.push(p)
            console.log(p)
          }
          this.allSchedules.push(s)
        }
      })
      .catch((error) => {
        console.log(error)
      })
  }
```
# Schedule Create 

Создание нового расписания

**URL** : `/createschedule`

**Methods** : `POST`

## Success Responses

**Code** : `201 Created`

**Content** : `{}`

```javascript
async addSchedule () {
      this.form1.group = this.group
      await this.axios
        .post('http://127.0.0.1:8000/college/schedule/create/', this.form1)
        .then((res) => {
          console.log(res)
        })
        .catch((error) => {
          console.log(error)
        })
      await this.axios
        .get('http://127.0.0.1:8000/college/schedules')
        .then((res) => {
          this.form2.schedule = res.data.length + 13
        })
        .catch((error) => {
          console.log(error)
        })
      for (const pair of this.pairs) {
        if (pair.group === this.group) {
          this.form2.pair = pair.id
          console.log(this.form2)
          await this.axios
            .post('http://127.0.0.1:8000/college/schedule/addpairs/', this.form2)
            .then((res) => {
              console.log(res)
            })
            .catch((error) => {
              console.log(error)
            })
        }
      }
      window.location.href = '/schedules'
    }
  }
```
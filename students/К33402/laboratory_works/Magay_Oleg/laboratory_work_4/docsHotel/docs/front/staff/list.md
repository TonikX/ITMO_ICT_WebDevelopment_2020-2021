# Staff List

Просмотреть данные о персонале

**URL** : `/staff/`

**Methods** : `GET`

## Success Responses

**Code** : `200 OK`

**Content** : `[{}]`

```javascript
    this.axios
      .get('http://127.0.0.1:8000/staff/list/')
      .then((res) => {
        this.staff = res.data
      })
      .catch((error) => {
        console.log(error)
      })
}
```
# Guest list

Список гостей

**URL** : `/`

**Methods** : `GET`

## Success Responses

**Code** : `200 OK`

**Content** : `[{}]`

```javascript
    this.axios
      .get('http://127.0.0.1:8000/guest/list/')
      .then((res) => {
        this.guests = res.data
      })
      .catch((error) => {
        console.log(error)
      })
}
```
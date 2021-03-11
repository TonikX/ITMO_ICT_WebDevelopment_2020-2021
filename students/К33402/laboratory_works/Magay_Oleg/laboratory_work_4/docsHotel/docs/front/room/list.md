# Room List

Просмотреть список номеров 

**URL** : `/room/`

**Methods** : `GET`

## Success Responses

**Code** : `200 OK`

**Content** : `[{}]`

```javascript
    this.axios
      .get('http://127.0.0.1:8000/room/list/')
      .then((res) => {
        this.rooms = res.data
      })
      .catch((error) => {
        console.log(error)
      })
}
```
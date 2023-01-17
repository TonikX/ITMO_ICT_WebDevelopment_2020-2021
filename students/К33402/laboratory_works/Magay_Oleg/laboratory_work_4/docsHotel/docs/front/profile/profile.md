# Profile

Профиль пользователя

**URL** : `/profile`

**Methods** : `PUT`

## Success Responses

**Code** : `200 OK`

**Content** : `{}`

```javascript
    async update (el) {
      await this.axios
        .put('http://127.0.0.1:8000/auth/users/me/', this.addForm)
        .then((res) => {
          console.log(res)
          this.$router.go()
        })
        .catch((error) => {
          console.log(error)
          alert('Похоже, вы ввели некорректный email!')
        })
    }
}
```
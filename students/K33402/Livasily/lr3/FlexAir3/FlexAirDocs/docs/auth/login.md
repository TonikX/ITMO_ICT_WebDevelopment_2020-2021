# login user

Авторизирует юзера

**URL** : `/user/login/`

**Methods** : `POST`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```javascript
export const login = (username, password) => dispatch =>{

    const config = {
        headers: {
            "Content-Type": 'application/json'
        }
    }

    const body = JSON.stringify({username, password})

    axios.post('/api/auth/login', body, config).then(res => {
        dispatch({
            type: LOGIN_SUCCESS,
            payload: res.data
        })
    }).catch(err => {console.log(err)})
}
```


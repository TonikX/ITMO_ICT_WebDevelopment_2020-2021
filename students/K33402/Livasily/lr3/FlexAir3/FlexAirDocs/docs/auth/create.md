# Create user

Создает нового пользователя

**URL** : `/aoth/create/`

**Methods** : `POST`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```javascript
export const register = ({username, password, email}) => dispatch => {

    const config = {
        headers: {
            "Content-Type": 'application/json'
        }
    }

    const body = JSON.stringify({username, email, password})

    axios.post('/api/auth/register', body, config).then(res => {
        dispatch({
            type: REGISTER_SUCCESS,
            payload: res.data
        })
    }).catch(err => {console.log(err)})
}
```




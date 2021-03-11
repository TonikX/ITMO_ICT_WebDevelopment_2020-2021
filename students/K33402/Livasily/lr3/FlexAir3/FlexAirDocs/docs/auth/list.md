# List of all users

Выводит информацию обо всех пользователях

**URL** : `/users/list/`

**Method** : `GET`

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```javascript
export const loadUser = () => (dispatch, getState) =>{
    // dispatch({type: USER_LOADING})

    axios.get('/api/auth/user',  tokenConfig(getState)).then(res => {
        dispatch({
            type: USER_LOADED,
            payload: res.data
        })
    }).catch(err => console.log(err))
}
```

```json
    "id": ,
    "username": ""
```
# logout User

выоходит из под юзера

**URL** : `/user/logout/`

**Methods** : `POST`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```javascript

export const logoutUser = () => (dispatch, getState) =>{

    const token = getState().auth.token

    const config = {
        headers: {
            "Content-Type": 'application/json'
        }
    }
    //IF token, add too header config
    if(token){
        config.headers['Authorization'] = `Token ${token}`
    }

    axios.post('/api/auth/logout/', null, tokenConfig(getState)).then(res => {
        dispatch({
            type: LOGOUT_SUCCESS,
        })
    }).catch(err => console.log(err))
}
```


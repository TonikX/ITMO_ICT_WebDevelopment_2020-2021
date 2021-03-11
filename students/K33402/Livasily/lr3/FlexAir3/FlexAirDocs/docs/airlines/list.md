# List of all airlines

Выводит информацию обо всех Компаниях

**URL** : `/airline/list/`

**Method** : `GET`

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```javascript
export const getAirlines = () => (dispatch, getState) =>{
    axios.get('/api/airlines/',tokenConfig(getState))
        .then(res => {
            dispatch({
                type: GET_AIRLINES,
                payload: res.data
            })
        }).catch(err => console.log(err))
}
```

```json
{
  "id": ""
  "name": "",
  "owner": ""
}

```
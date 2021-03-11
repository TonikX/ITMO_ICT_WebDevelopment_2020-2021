# Create Airline

Создает новый аэропорт

**URL** : `/airlines/create/`

**Methods** : `POST`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```javascript
    export const addAirplanes = (airline) => (dispatch, getState) => {
    axios.post(`/api/airlines/`, airline, tokenConfig(getState)).then(res => {
        dispatch({
            type: ADD_AIRLANES,
            payload: res.data
        })
    }).catch(err => {console.log(err)})
}
```




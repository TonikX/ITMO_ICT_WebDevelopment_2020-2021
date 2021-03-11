# Delete Airline

удаляет аэропорт

**URL** : `/airlines/delete/`

**Methods** : `DELETE`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```javascript
  export const deleteAirlines = id => (dispatch, getState) =>{
    axios.delete(`/api/airlines/${id}`, tokenConfig(getState))
        .then(res => {
            dispatch({
                type: DELETE_AIRLINES,
                payload: id
            })
        }).catch(err => console.log(err))
}
```




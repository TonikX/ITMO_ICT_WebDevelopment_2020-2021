# List of all route

Выводит информацию обо всех маршрутах

**URL** : `/Route/list/`

**Method** : `GET`

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
  {
    "id": 1,
    "dateDeparture": "2021-01-05T16:06:44Z",
    "dateArrival": "2021-01-06T16:06:46Z",
    "distance": 7000000,
    "departure": 1,
    "arrival": 1
  }
]
```
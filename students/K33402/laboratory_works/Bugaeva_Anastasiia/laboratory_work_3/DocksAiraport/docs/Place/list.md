# List of all Place

Выводит информацию обо всех зарезервированных местах

**URL** : `/placeGet`

**Method** : `GET`

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
  {
        "id": 1,
        "passenger": {
            "username": "panda0412",
            "first_name": "Anastasiia",
            "last_name": "Bugaeva"
        },
        "num_flight": {
            "id": 1,
            "num_flight": 10,
            "numberOfPackages": 125,
            "departure_date": "2021-04-17T06:57:10Z",
            "arrival_date": "2021-04-17T09:57:11Z",
            "company": {
                "id": 1,
                "name": "S7"
            },
            "departure": {
                "id": 1,
                "cityName": "Москва",
                "airportName": "Домодедово"
            },
            "arrival": {
                "id": 3,
                "cityName": "Саратов",
                "airportName": "Гагарин"
            }
        }
    }
]
```

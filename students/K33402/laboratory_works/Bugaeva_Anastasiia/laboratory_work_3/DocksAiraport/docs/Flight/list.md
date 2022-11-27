# List of all Flight

Выводит информацию обо всех рейсах

**URL** : `/flightGet`

**Method** : `GET`

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "id": 1,
        "arrival": {
            "id": 3,
            "cityName": "Саратов",
            "airportName": "Гагарин"
        },
        "departure": {
            "id": 1,
            "cityName": "Москва",
            "airportName": "Домодедово"
        },
        "company": {
            "id": 1,
            "name": "S7"
        },
        "numberFlight": [
            {
                "passenger": {
                    "username": "panda0412",
                    "first_name": "Anastasiia",
                    "last_name": "Bugaeva"
                }
            }
        ],
        "Flight": [
            {
                "rating": 7,
                "author": {
                    "username": "panda0412",
                    "first_name": "Anastasiia",
                    "last_name": "Bugaeva"
                },
                "text": "Всё супер! Ну почти.."
            }
        ],
        "num_flight": 10,
        "numberOfPackages": 125,
        "departure_date": "2021-04-17T06:57:10Z",
        "arrival_date": "2021-04-17T09:57:11Z"
    }
]
```

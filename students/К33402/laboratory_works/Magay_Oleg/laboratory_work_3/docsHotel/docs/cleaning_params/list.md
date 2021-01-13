### Просмотреть данные о возможном графике работы сотрудников

**URL** : `/cleaning_params/list/`

**HTTP 200 OK**

**Allow** : GET, HEAD, OPTIONS

**Content-Type** : application/json

**Vary** : Accept

**JSON** :
```json
[
    {
        "id": 1,
        "day": "mon",
        "floor": 1
    },
    {
        "id": 2,
        "day": "tue",
        "floor": 1
    },
    {
        "id": 3,
        "day": "thu",
        "floor": 2
    }
]
```
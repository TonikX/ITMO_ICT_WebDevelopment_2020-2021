### Просмотреть данные о постояльцах

**URL** : `/guest/list/`

**HTTP 200 OK**

**Allow** : GET, HEAD, OPTIONS

**Content-Type** : application/json

**Vary** : Accept

**JSON** :
```json
[
    {
        "id": 1,
        "passport": 123456,
        "first_name": "ivanov",
        "last_name": "ivan",
        "middle_name": "ivanovich",
        "city": "moscow",
        "start_date": "2021-01-06",
        "room": 2
    },
    {
        "id": 2,
        "passport": 123456,
        "first_name": "nikitin",
        "last_name": "nikita",
        "middle_name": "nikitovich",
        "city": "spb",
        "start_date": "2021-01-06",
        "room": 1
    }
]
```
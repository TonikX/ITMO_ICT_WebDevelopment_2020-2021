### Просмотреть данные о графике работы сотрудников

**URL** : `/staff_cleaning/list/`

**HTTP 200 OK**

**Allow** : GET, HEAD, OPTIONS

**Content-Type** : application/json

**Vary** : Accept

**JSON** :
```json
[
    {
        "id": 1,
        "staff": 1,
        "params": 1
    },
    {
        "id": 2,
        "staff": 1,
        "params": 3
    },
    {
        "id": 3,
        "staff": 1,
        "params": 2
    }
]
```
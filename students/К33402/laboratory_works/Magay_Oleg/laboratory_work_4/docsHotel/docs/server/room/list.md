### Просмотреть данные о номерах

**URL** : `/room/list/`

**HTTP 200 OK**

**Allow** : GET, HEAD, OPTIONS

**Content-Type** : application/json

**Vary** : Accept

**JSON** :
```json
[
    {
        "id": 1,
        "number": 123,
        "type": "one",
        "cost": 200,
        "phone": "34-78-90",
        "status": "busy",
        "total": 400
    },
    {
        "id": 2,
        "number": 456,
        "type": "two",
        "cost": 500,
        "phone": "34-90-90",
        "status": "free",
        "total": 0
    }
]
```
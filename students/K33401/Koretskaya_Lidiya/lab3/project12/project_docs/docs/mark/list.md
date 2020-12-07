### Просмотреть данные об оценке студента 

**URL** : `/mark/list/`

**HTTP 200 OK**

**Allow** : GET, HEAD, OPTIONS

**Content-Type** : application/json

**Vary** : Accept

**JSON** :
```json
[
    {
        "id": 1,
        "mark": 4,
        "student": 1,
        "subject": 1
    },
    {
        "id": 2,
        "mark": 5,
        "student": 2,
        "subject": 3
    }
]
```
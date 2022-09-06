### Просмотреть данные о преподавателе 

**URL** : `/teacher/list/`

**HTTP 200 OK**

**Allow** : GET, HEAD, OPTIONS

**Content-Type** : application/json

**Vary** : Accept

**JSON** :
```json
[
    {
        "id": 1,
        "subjects": [
            {
                "name": "bio"
            },
            {
                "name": "rus"
            }
        ],
        "first_name": "nina",
        "last_name": "ivanova",
        "room": "12"
    }
]
```
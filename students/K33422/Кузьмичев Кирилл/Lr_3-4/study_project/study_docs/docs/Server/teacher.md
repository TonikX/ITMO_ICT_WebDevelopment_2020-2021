## Преподаватель

### Добавление

**URL** : `/teacher/create/`

**HTTP 201 Created**

**Allow** : POST, OPTIONS

**Content-Type** : application/json

**Vary** : Accept

**JSON** :
```json
{
    "id": 1,
    "subjects": [],
    "first_name": "nina",
    "last_name": "ivanova",
    "room": "12"
}
```

### Просмотр

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

### Изменение/удаление

**URL** : `/teacher/1/`

**HTTP 200 OK**

**Allow** : GET, PUT, PATCH, DELETE, HEAD, OPTIONS

**Content-Type** : application/json

**Vary** : Accept

**JSON** :
```json
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
```
## Студент

### Добавление

**URL** : `/student/create/`

**HTTP 201 Created**

**Allow** : POST, OPTIONS

**Content-Type** : application/json

**Vary** : Accept

**JSON** :
```json
{
    "id": 1,
    "first_name": "misha",
    "last_name": "misha",
    "group": "1"
}
```

### Просмотр

**URL** : `/student/list/`

**HTTP 200 OK**

**Allow** : GET, HEAD, OPTIONS

**Content-Type** : application/json

**Vary** : Accept

**JSON** :
```json
[
    {
        "id": 1,
        "first_name": "misha",
        "last_name": "misha",
        "group": "1"
    },
    {
        "id": 2,
        "first_name": "lena",
        "last_name": "lenina",
        "group": "2"
    }
]
```

### Изменение/удаление

**URL** : `/student/1/`

**HTTP 200 OK**

**Allow** : GET, PUT, PATCH, DELETE, HEAD, OPTIONS

**Content-Type** : application/json

**Vary** : Accept

**JSON** :
```json
{
    "id": 1,
    "first_name": "misha",
    "last_name": "misha",
    "group": "1"
}
```
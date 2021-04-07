## Предмет

### Добавление

**URL** : `/subject/create/`

**HTTP 201 Created**

**Allow** : POST, OPTIONS

**Content-Type** : application/json

**Vary** : Accept

**JSON** :
```json
{
    "id": 3,
    "name": "rus"
}
```

## Просмотр

**URL** : `/subject/list/`

**HTTP 200 OK**

**Allow** : GET, HEAD, OPTIONS

**Content-Type** : application/json

**Vary** : Accept

**JSON** :
```json
[
    {
        "id": 1,
        "name": "bio"
    },
    {
        "id": 2,
        "name": "math"
    },
    {
        "id": 3,
        "name": "rus"
    }
]
```

### Изменение/удаление

**URL** : `/subject/1/`

**HTTP 200 OK**

**Allow** : GET, PUT, PATCH, DELETE, HEAD, OPTIONS

**Content-Type** : application/json

**Vary** : Accept

**JSON** :
```json
{
    "id": 1,
    "name": "bio"
}
```
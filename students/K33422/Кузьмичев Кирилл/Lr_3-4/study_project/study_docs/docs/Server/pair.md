## Пара

### Добавление

**URL** : `/pair/create/`

**HTTP 201 Created**

**Allow** : POST, OPTIONS

**Content-Type** : application/json

**Vary** : Accept

**JSON** :
```json
{
    "id": 2,
    "group": "1",
    "pair_number": 2,
    "name_day": "mon",
    "room": 211,
    "teacher": 1,
    "subject": 3
}
```

### Просмотр

**URL** : `/pair/list/`

**HTTP 200 OK**

**Allow** : GET, HEAD, OPTIONS

**Content-Type** : application/json

**Vary** : Accept

**JSON** :
```json
[
    {
        "id": 1,
        "group": "1",
        "pair_number": 1,
        "name_day": "mon",
        "room": 123,
        "teacher": 1,
        "subject": 1
    },
    {
        "id": 2,
        "group": "1",
        "pair_number": 2,
        "name_day": "mon",
        "room": 211,
        "teacher": 1,
        "subject": 3
    }
]
```

### Изменение/удаление

**URL** : `/pair/1/`

**HTTP 200 OK**

**Allow** : GET, PUT, PATCH, DELETE, HEAD, OPTIONS

**Content-Type** : application/json

**Vary** : Accept

**JSON** :
```json
{
    "id": 1,
    "group": "1",
    "pair_number": 1,
    "name_day": "mon",
    "room": 123,
    "teacher": 1,
    "subject": 1
}
```
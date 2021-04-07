### Оценка

### Добавление

**URL** : `/mark/create/`

**HTTP 201 Created**

**Allow** : POST, OPTIONS

**Content-Type** : application/json

**Vary** : Accept

**JSON** :
```json
{
    "id": 2,
    "mark": 5,
    "student": 2,
    "subject": 3
}
```

### Просмотр

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

### Изменение/удаление

**URL** : `/mark/1/`

**HTTP 200 OK**

**Allow** : GET, PUT, PATCH, DELETE, HEAD, OPTIONS

**Content-Type** : application/json

**Vary** : Accept

**JSON** :
```json
{
    "id": 1,
    "mark": 4,
    "student": 1,
    "subject": 1
}
```
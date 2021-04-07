## Предметы преподавателя

### Добавление

**URL** : `/subteach/create/`

**HTTP 201 Created**

**Allow** : POST, OPTIONS

**Content-Type** : application/json

**Vary** : Accept

**JSON** :
```json
{
    "id": 2,
    "subject": 3,
    "teacher": 1
}
```

### Просмотр

**URL** : `/subteach/list/`

**HTTP 200 OK**

**Allow** : GET, HEAD, OPTIONS

**Content-Type** : application/json

**Vary** : Accept

**JSON** :
```json
[
    {
        "id": 1,
        "subject": 1,
        "teacher": 1
    },
    {
        "id": 2,
        "subject": 3,
        "teacher": 1
    }
]
```

### Изменение/удаление

**URL** : `/subteach/1/`

**HTTP 200 OK**

**Allow** : GET, PUT, PATCH, DELETE, HEAD, OPTIONS

**Content-Type** : application/json

**Vary** : Accept

**JSON** :
```json
{
    "id": 2,
    "subject": 3,
    "teacher": 1
}
```
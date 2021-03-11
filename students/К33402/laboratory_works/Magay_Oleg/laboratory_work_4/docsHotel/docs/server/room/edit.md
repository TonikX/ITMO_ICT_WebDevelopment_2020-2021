### Изменить/удалить данные о номере

**URL** : `/room/1/`

**HTTP 200 OK**

**Allow** : GET, PUT, PATCH, DELETE, HEAD, OPTIONS

**Content-Type** : application/json

**Vary** : Accept

**JSON** :
```json
{
    "id": 1,
    "number": 123,
    "type": "one",
    "price": 200,
    "phone": "34-78-90",
    "status": "busy",
    "total": 400
}
```
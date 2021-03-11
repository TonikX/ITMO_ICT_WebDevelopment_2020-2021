### Изменить/удалить данные о постояльцах

**URL** : `/guest/2/`

**HTTP 200 OK**

**Allow** : GET, PUT, PATCH, DELETE, HEAD, OPTIONS

**Content-Type** : application/json

**Vary** : Accept

**JSON** :
```json
{
    "id": 2,
    "passport": 123456,
    "first_name": "nikitin",
    "last_name": "nikita",
    "middle_name": "nikitovich",
    "city": "spb",
    "start_date": "2021-01-06",
    "room": 1
}
```
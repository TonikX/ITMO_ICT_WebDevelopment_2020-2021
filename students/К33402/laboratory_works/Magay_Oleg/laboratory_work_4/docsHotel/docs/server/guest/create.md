### Добавить постояльцев

**URL** : `/guest/create/`

**HTTP 201 Created**

**Allow** : POST, OPTIONS

**Content-Type** : application/json

**Vary** : Accept

**JSON** :
```json
{
    "id": 1,
    "passport": 123456,
    "first_name": "ivanov",
    "last_name": "ivan",
    "middle_name": "ivanovich",
    "city": "moscow",
    "start_date": "2021-01-06",
    "room": 2
}
```
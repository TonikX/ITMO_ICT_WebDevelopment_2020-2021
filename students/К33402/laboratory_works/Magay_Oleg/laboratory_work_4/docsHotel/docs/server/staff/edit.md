### Изменить/удалить данные о сотруднке

**URL** : `/staff/1/`

**HTTP 200 OK**

**Allow** : GET, PUT, PATCH, DELETE, HEAD, OPTIONS

**Content-Type** : application/json

**Vary** : Accept

**JSON** :
```json
{
    "id": 1,
    "cleaning": [
        {
            "day": "mon",
            "floor": 1
        },
        {
            "day": "thu",
            "floor": 2
        },
        {
            "day": "tue",
            "floor": 1
        }
    ],
    "first_name": "kitov",
    "last_name": "maxim",
    "middle_name": "ivanov"
}
```
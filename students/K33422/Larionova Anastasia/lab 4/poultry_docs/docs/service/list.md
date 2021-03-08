# List of all services

Выводит информацию обо всех зарегистрированных обслуживаниях

**URL** : `/services/list/`

**Method** : `GET`

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "id": 1,
        "username": "firstuser",
        "cell": "15",
        "status": true
    },
    {
        "id": 2,
        "username": "tomjones",
        "cell": "15",
        "status": true
    }
]
```
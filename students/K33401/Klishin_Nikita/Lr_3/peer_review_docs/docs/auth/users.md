# Показать всех пользователей

Выводит информацию о всех пользователях системы

**URL** : `/auth/users/`

**Method** : `GET`

**Auth required** : YES

## Success Responses

**Code** : `200 OK`

**Data** :

```json
[
    {
        "is_teacher": false,
        "id": 1,
        "email": "klishin.nd16@gmail.com"
    },
    {
        "is_teacher": false,
        "id": 2,
        "email": "klishin.nd17@gmail.com"
    },
    {
        "is_teacher": false,
        "id": 3,
        "email": "klishin.nd18@gmail.com"
    }
]
```
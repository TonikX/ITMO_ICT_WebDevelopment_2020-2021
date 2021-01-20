# Показать студентов

Выводит список студентов в системе.
Позволяет добавлять профили студентов.

**URL** : `/api/students/`

**Methods** : `GET`, `POST`

**Auth required** : YES

## Success Responses

**Code** : `200 OK`

**Data** :

```json
[
    {
        "id": 1,
        "user": {
            "email": "klishin.nd16@gmail.com",
            "is_teacher": false
        }
    },
    {
        "id": 2,
        "user": {
            "email": "klishin.nd18@gmail.com",
            "is_teacher": false
        }
    }
]
```
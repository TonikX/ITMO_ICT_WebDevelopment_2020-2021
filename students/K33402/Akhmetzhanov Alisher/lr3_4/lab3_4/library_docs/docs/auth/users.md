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
        "id": 1,
        "email": "ivanov@gmail.com",
        "is_librarian": false
    },
    {
        "id": 2,
        "email": "petrov@gmail.com",
        "is_librarian": false
    },
    {
        "email": "lebedev@gmail.com",
        "id": 3,
        "is_librarian": false
    }
]
```
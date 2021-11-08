# Книги читального зала

Выводит список читателей выбранного зала.

**URL** : `/api/library_hall/<int:pk>/copies/`

**Methods** : `GET, PATCH`

**Auth required** : YES

## Success Responses

**Code** : `200 OK`

**Data** :

```json
[
    {
        "id": 2,
        "user": {
            "id": 2,
            "email": "ivanov@gmail.com",
            "first_name": "",
            "last_name": "",
            "is_librarian": true
        },
        "reader_ticket": 7,
        "passport": "1234 343554",
        "birth_date": "2021-01-22",
        "address": "fdfd",
        "phone": "+79158541912",
        "is_scientist": false,
        "hall": 1
    },
    {
        "id": 4,
        "user": {
            "id": 1,
            "email": "petrov@gmail.com",
            "first_name": "Иван",
            "last_name": "Петров",
            "is_librarian": false
        },
        "reader_ticket": 14,
        "passport": "1234 343554",
        "birth_date": "2021-01-22",
        "address": "Буниdfd",
        "phone": "+79158541917fd",
        "is_scientist": false,
        "hall": 1
    }
]
```
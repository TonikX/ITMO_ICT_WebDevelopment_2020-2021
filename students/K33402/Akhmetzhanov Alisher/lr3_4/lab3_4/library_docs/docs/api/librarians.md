# Библиотекари

Выводит список библиотекарей в библиотеке

**URL** : `/api/librarians/`

**Methods** : `GET`, `POST`

**Auth required** : YES

## Success Responses

**Code** : `200 OK`

**Data** :

```json
[
    {
        "user": {
            "id": 2,
            "email": "klishin.nd17@gmail.com",
            "first_name": "",
            "last_name": "",
            "is_librarian": true
        },
        "experience": "Опыт есть"
    }
]
```
# Книги

Выводит информацию о всех книгах в библиотеке

**URL** : `/api/books/`

**Methods** : `GET`, `POST`

**Auth required** : YES

## Success Responses

**Code** : `200 OK`

**Data** :

```json
[
    {
        "id": 1,
        "title": "Война и мир",
        "author": "Л. Толстой",
        "realise_date": "1850-01-22",
        "publishing_house": "Медиа"
    },
    {
        "id": 2,
        "title": "Преступление и наказание",
        "author": "Достоевский",
        "realise_date": "2021-01-26",
        "publishing_house": "Медиа"
    },
    {
        "id": 3,
        "title": "Эрагон",
        "author": "Кристофер Паолини",
        "realise_date": "2021-01-29",
        "publishing_house": "РусКнига"
    }
]
```
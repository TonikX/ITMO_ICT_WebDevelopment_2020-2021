# Книга

Выводит подробную информацию о книге.
Позволяет изменять текущую книгу.

**URL** : `/api/book/<pk>/`

**Methods** : `GET`, `PATCH`

**Auth required** : YES

## Success Responses

**Code** : `200 OK`

**Data** :

```json
{
    "id": 1,
    "title": "Война и мир",
    "author": "Толстой",
    "realise_date": "1850-01-22",
    "publishing_house": "Медиа"
}
```
# Показать проверяющих

Выводит список проверяющих для текущей задачи.
Позволяет добавлять новых проверяющих.

**URL** : `/api/task/<pk>/inspectors/`

**Methods** : `GET`, `POST`

**Auth required** : YES

## Success Responses

**Code** : `200 OK`

**Data** :

```json
[
    {
        "email": "klishin.nd17@gmail.com",
        "is_teacher": false
    }
]
```
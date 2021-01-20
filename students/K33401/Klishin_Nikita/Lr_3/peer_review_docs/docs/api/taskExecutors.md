# Показать исполнителей

Выводит список исполнителей текущей задачи.
Позволяет добавлять новых исполнителей с определением сроков сдачи задания.

**URL** : `/api/task/<pk>/executors/`

**Methods** : `GET`, `POST`

**Auth required** : YES

## Success Responses

**Code** : `200 OK`

**Data** :

```json
[
    {
        "email": "klishin.nd16@gmail.com",
        "is_teacher": false
    },
    {
        "email": "klishin.nd17@gmail.com",
        "is_teacher": false
    }
]
```
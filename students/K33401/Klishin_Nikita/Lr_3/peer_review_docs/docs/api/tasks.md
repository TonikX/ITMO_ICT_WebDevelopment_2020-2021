# Показать задачи

Выводит информацию о всех созданных задачах в системе.
Также позволяет создавать новые задачи.

**URL** : `/api/tasks/`

**Methods** : `GET`, `POST`

**Auth required** : YES

## Success Responses

**Code** : `200 OK`

**Data** :

```json
[
    {
        "id": 1,
        "title": "Задание 1",
        "description": "Описание задания 2",
        "status": 0,
        "criterions": [
            1,
            2
        ],
        "executors": [
            1,
            2
        ],
        "inspections": [
            2
        ]
    }
]
```
# Показать задачу

Выводит подробную информацию о конкретной задаче.
Позволяет изменять и удалять текущую задачу.

**URL** : `/api/task/<pk>/`

**Methods** : `GET`, `POST`, `DELETE`

**Auth required** : YES

## Success Responses

**Code** : `200 OK`

**Data** :

```json
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
```
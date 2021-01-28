# Показать задачи для текущего пользователя

Выводит список задач для проверки для текущего пользвателя.

**URL** : `/api/my_inspection_tasks/`

**Methods** : `GET`

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
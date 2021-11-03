# Показать список всех умений

Выводит информацию обо всех умениях.

**URL** : `war/skills/`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

**Success info** : HTTP 200 OK

**Content-Type** : application/json

**JSON** :
```json
{
    "Skills": [
        {
            "id": 1,
            "title": "Операционные системы"
        },
        {
            "id": 2,
            "title": "Django"
        },
        {
            "id": 3,
            "title": "Git"
        },
        {
            "id": 4,
            "title": "Vue"
        },
        {
            "id": 5,
            "title": "Автоматизация тестирования"
        }
    ]
}
```

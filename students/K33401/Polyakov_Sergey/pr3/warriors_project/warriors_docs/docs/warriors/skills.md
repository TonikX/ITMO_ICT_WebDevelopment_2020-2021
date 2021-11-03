# Вывести список воинов и умений

Выводит информацию обо всех воинах и их умениях.

**URL** : `war/warriors_skills/`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

**Success info** : HTTP 200 OK

**Content-Type** : application/json

**JSON** :
```json
{
    "Warriors with skills": [
        {
            "id": 2,
            "skills": [
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
                }
            ],
            "race": "d",
            "name": "Иван",
            "level": 2,
            "profession": 2
        },
        {
            "id": 3,
            "skills": [
                {
                    "id": 1,
                    "title": "Операционные системы"
                },
                {
                    "id": 3,
                    "title": "Git"
                },
                {
                    "id": 4,
                    "title": "Vue"
                }
            ],
            "race": "d",
            "name": "Петр",
            "level": 5,
            "profession": 3
        }
    ]
}
```

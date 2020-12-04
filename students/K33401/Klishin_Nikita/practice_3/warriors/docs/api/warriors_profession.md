# Показать воинов и их профессии

Выводит список войнов с их профессиями

**URL** : `/api/warriors_profession/`

**Method** : `GET`

<!-- **Auth required** : YES -->

**Permissions required** : None

<!-- **Data constraints** : `{}` -->

## Success Responses

**Code** : `200 OK`

<!-- **Content** : `{[]}` -->

```json
{
   [
    {
        "id": 1,
        "profession": {
            "id": 1,
            "title": "swordsman",
            "description": "Fights with sword"
        },
        "race": "s",
        "name": "Student1",
        "level": 7,
        "skill": [
            2
        ]
    },
    {
        "id": 2,
        "profession": {
            "id": 1,
            "title": "swordsman",
            "description": "Fights with sword"
        },
        "race": "d",
        "name": "Developer 1",
        "level": 7,
        "skill": [
            1
        ]
    }
]
}
```
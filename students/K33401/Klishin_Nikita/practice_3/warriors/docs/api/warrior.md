# Показать подробную информацию о воине

Выводит подробную информацию о воине

**URL** : `/api/warrior/{id}`

**Method** : `GET`

<!-- **Auth required** : YES -->

**Permissions required** : None

<!-- **Data constraints** : `{}` -->

## Success Responses

**Code** : `200 OK`

<!-- **Content** : `{[]}` -->

```json
{
    "id": 1,
    "profession": {
        "id": 1,
        "title": "swordsman",
        "description": "Fights with sword"
    },
    "skill": [
        {
            "id": 2,
            "title": "Water"
        }
    ],
    "race": "student",
    "name": "Student1",
    "level": 7
}
```
# Показать всех воинов и их профессии

**URL** : `/war/war_list/prof/`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "Warriors and their profs": [
        {
            "id": 1,
            "profession": {
                "title": "mobile developer",
                "description": "making mobile apps"
            },
            "race": "s",
            "name": "Nick",
            "level": 1,
            "skill": [
                1
            ]
        },
        {
            "id": 2,
            "profession": {
                "title": "frontend",
                "description": "front"
            },
            "race": "d",
            "name": "Mary",
            "level": 5,
            "skill": [
                2
            ]
        },
        {
            "id": 3,
            "profession": {
                "title": "DS",
                "description": "Data Science"
            },
            "race": "t",
            "name": "Ann",
            "level": 10,
            "skill": [
                2
            ]
        },
        {
            "id": 4,
            "profession": {
                "title": "web dev",
                "description": "web developer"
            },
            "race": "d",
            "name": "Paul",
            "level": 7,
            "skill": [
                3
            ]
        }
    ]
}
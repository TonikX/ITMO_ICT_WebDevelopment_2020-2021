# Вывести список воинов и их профессии 

Вывод полной информации о всех войнах и их профессиях (в одном запросе).

**URL** : `war/warriors/profession/`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

**Success info** : HTTP 200 OK

**Content-Type** : application/json

**JSON** :
```json
    {
        "id": 2,
        "profession": {
            "title": "kill",
            "description": "kill"
        },
        "race": "teamlead",
        "name": "kkk",
        "level": 9,
        "skill": []
    },
    {
        "id": 3,
        "profession": {
            "title": "Driver",
            "description": "Dive"
        },
        "race": "teamlead",
        "name": "oleg",
        "level": 4,
        "skill": [
            1
        ]
    }
```
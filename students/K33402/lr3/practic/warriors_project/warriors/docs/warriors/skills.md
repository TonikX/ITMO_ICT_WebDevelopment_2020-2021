# Вывести список воинов и умений

Выводит информацию обо всех воинах и их умениях.

**URL** : `warriors/skills/`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

**Success info** : HTTP 200 OK

**Content-Type** : application/json

**JSON** :
```json
{
        "name": "Pro",
        "skill": [
            "Strategy",
            "Force",
            "Beauty",
            "Charisma",
            "Leadership"
        ]
    },
    {
        "name": "Sally",
        "skill": [
            "Leadership",
            "Force"
        ]
    }
```
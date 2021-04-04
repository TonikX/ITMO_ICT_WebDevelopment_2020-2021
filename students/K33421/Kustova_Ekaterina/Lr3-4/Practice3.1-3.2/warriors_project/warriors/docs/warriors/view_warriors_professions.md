# Список всех воинов и их профессий

###Вывод информации о всех воинах и их профессиях 

**URL** : `warriors_professions/`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

**Success info** : HTTP 200 OK

**Content-Type** : application/json

**JSON** :
```json
{
    "Professions": [
        {
            "id": 1,
            "profession": {
                "title": "Profession1",
                "description": "description1"
            },
            "race": "s",
            "name": "Warrior",
            "level": 1
        }
    ]
}
```
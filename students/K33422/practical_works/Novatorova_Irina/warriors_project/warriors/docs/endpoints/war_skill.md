# Показать всех воинов и их скилы

**URL** : `/war/war_list/skill/`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "Warriors and their skills": [
        {
            "id": 1,
            "skill": [
                {
                    "id": 1,
                    "title": "java"
                }
            ],
            "race": "s",
            "name": "Nick",
            "level": 1,
            "profession": 1
        },
        {
            "id": 2,
            "skill": [
                {
                    "id": 2,
                    "title": "python"
                }
            ],
            "race": "d",
            "name": "Mary",
            "level": 5,
            "profession": 4
        },
        {
            "id": 3,
            "skill": [
                {
                    "id": 2,
                    "title": "python"
                }
            ],
            "race": "t",
            "name": "Ann",
            "level": 10,
            "profession": 2
        },
        {
            "id": 4,
            "skill": [
                {
                    "id": 3,
                    "title": "c++"
                }
            ],
            "race": "d",
            "name": "Paul",
            "level": 7,
            "profession": 3
        }
    ]
}
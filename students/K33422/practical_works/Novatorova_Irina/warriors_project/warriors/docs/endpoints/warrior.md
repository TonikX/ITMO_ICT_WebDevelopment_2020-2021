# Показать всех воинов

Выводит информацию обо всех войнах

**URL** : `/war/warrior/`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`


```json
{
    "Warriors": [
        {
            "id": 1,
            "race": "s",
            "name": "Nick",
            "level": 1,
            "profession": 1,
            "skill": [
                1
            ]
        },
        {
            "id": 2,
            "race": "d",
            "name": "Mary",
            "level": 5,
            "profession": 4,
            "skill": [
                2
            ]
        },
        {
            "id": 3,
            "race": "t",
            "name": "Ann",
            "level": 10,
            "profession": 2,
            "skill": [
                2
            ]
        },
        {
            "id": 4,
            "race": "d",
            "name": "Paul",
            "level": 7,
            "profession": 3,
            "skill": [
                3
            ]
        }
    ]
}
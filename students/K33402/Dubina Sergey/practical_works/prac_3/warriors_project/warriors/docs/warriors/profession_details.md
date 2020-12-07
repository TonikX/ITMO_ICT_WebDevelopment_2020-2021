Выводит информацию обо всех войнах и их профессиях

**URL** : `/war/warriors/profession_details`

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
        "profession": {
            "title": "Банкир",
            "description": "Очень важный"
        },
        "race": "student",
        "skill": [
            "Hustle",
            "Money generation"
        ],
        "name": "Burne",
        "level": 3
    }
]
}
```

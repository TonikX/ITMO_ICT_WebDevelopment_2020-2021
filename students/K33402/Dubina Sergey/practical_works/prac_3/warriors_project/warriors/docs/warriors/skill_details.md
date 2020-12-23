Выводит информацию обо всех войнах и их скиллах

**URL** : `/war/warriors/skills_details`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "Skills": [
        {
            "title": "Hustle",
            "skilled_warriors": [
                {
                    "id": 1,
                    "profession": "Банкир",
                    "race": "student",
                    "skill": [
                        "Hustle",
                        "Money generation"
                    ],
                    "name": "Burne",
                    "level": 3
                }
            ]
        },
        {
            "title": "Money generation",
            "skilled_warriors": [
                {
                    "id": 1,
                    "profession": "Банкир",
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
    ]
}
```

# List of all breeds

Выводит информацию обо всех породах

**URL** : `/breeds/list/`

**Method** : `GET`

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "id": 1,
        "breed": "Columbian",
        "productivity": "avg",
        "avg_weight": 3,
        "diet": "Vegetables & fruits"
    },
    {
        "id": 2,
        "breed": "Ameraucana",
        "productivity": "high",
        "avg_weight": 5,
        "diet": "Raw fruits and vegetables"
    }
]
```
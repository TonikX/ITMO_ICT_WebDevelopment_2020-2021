# List of all users

Выводит информацию обо всех пользователях

**URL** : `/users/list/`

**Method** : `GET`

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "first_name": "Nastya",
        "last_name": "Larionova",
        "username": "lanastya",
        "passport": "xx xxxxxx",
        "salary": 150000,
        "cell": []
    },
    {
        "first_name": "Ivan",
        "last_name": "Ivanov",
        "username": "firstuser",
        "passport": "7256 4629003",
        "salary": 10000,
        "cell": [
            2
        ]
    },
    {
        "first_name": "Anna",
        "last_name": "Miheeva",
        "username": "mihanna",
        "passport": null,
        "salary": 0,
        "cell": []
    },
    {
        "first_name": "Tom",
        "last_name": "Jones",
        "username": "tomjones",
        "passport": "7623 9822034",
        "salary": 30000,
        "cell": [
            2
        ]
    }
]
```
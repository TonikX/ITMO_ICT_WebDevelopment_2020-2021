# List of all user

Выводит информацию обо всех юзерах

**URL** : `/User/list/`

**Method** : `GET`

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
  {
    "first_name": "",
    "last_name": "",
    "username": "admin",
    "passport": ""
  },
  {
    "first_name": "Дмитрий",
    "last_name": "Замятин",
    "username": "dima",
    "passport": "0000000001"
  },
  {
    "first_name": "Ricardo",
    "last_name": "Milos",
    "username": "Ricardo",
    "passport": "0000000002"
  },
  {
    "first_name": "Вова",
    "last_name": "ВЛАДИМИРОВич",
    "username": "putya",
    "passport": "0000000003"
  },
  {
    "first_name": "Миша",
    "last_name": "Жмакин",
    "username": "misha",
    "passport": "0000000004"
  }
]
```
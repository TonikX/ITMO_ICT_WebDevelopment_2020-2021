# Просмотр пользователей


**URL** : `users/`

**Method** : `GET`

**Data constraints** : `{}`

**Success info** : HTTP 200 OK

**Content-Type** : application/json

**JSON** :

```json
[
    {
        "id": 1,
        "password": "pbkdf2_sha256$216000$1uaGyx5zUmcP$f4vjHGEly6PNyLZ6jBmRUsEtOaZ6n1yBlKM64ixHahs=",
        "last_login": "2021-01-16T14:59:32.172301Z",
        "is_superuser": false,
        "username": "User",
        "first_name": "",
        "last_name": "",
        "is_staff": false,
        "is_active": true,
        "date_joined": "2021-01-16T13:11:00.899829Z",
        "email": "User@mail.ru",
        "groups": [],
        "user_permissions": []
    },
    {
        "id": 2,
        "password": "pbkdf2_sha256$216000$7q48dKf2zKlj$hkbcxrKZO6zZiE/Xs2cnh9x9dp28JJP5Zb6EcbvxaKU=",
        "last_login": "2021-01-16T14:58:08.503961Z",
        "is_superuser": true,
        "username": "admin",
        "first_name": "",
        "last_name": "",
        "is_staff": true,
        "is_active": true,
        "date_joined": "2021-01-16T14:56:38.025352Z",
        "email": "admin@mail.ru",
        "groups": [],
        "user_permissions": []
    }
]
```
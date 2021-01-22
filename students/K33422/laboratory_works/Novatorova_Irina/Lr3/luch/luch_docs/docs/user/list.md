# Список пользователей

**URL** : `/luch/user/list/`

**Method** : `GET`

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "id": 2,
        "password": "pbkdf2_sha256$216000$T1iKzwipbgW1$DkPxaG+pz0fPDisKdDWhOZSh2dgCpum4QSGJoWEEQmQ=",
        "last_login": "2021-01-21T13:26:02.076366Z",
        "is_superuser": false,
        "username": "first",
        "is_staff": false,
        "is_active": true,
        "date_joined": "2021-01-21T13:23:08.034575Z",
        "first_name": null,
        "last_name": null,
        "email": "first@first.com",
        "groups": [],
        "user_permissions": []
    },
    {
        "id": 1,
        "password": "pbkdf2_sha256$216000$LgUBePonHR1O$3qigPeyRW4/9S/mkU6MoIH1w0raCOBK33Sn5oOydWq4=",
        "last_login": "2021-01-22T12:50:04.527251Z",
        "is_superuser": true,
        "username": "rina",
        "is_staff": true,
        "is_active": true,
        "date_joined": "2021-01-20T13:44:57.422033Z",
        "first_name": "",
        "last_name": "",
        "email": "admin@admin.com",
        "groups": [],
        "user_permissions": []
    }
]
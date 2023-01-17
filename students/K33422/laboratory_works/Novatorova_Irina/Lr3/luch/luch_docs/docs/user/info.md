# Просмотр/редактирование/удаление пользователя

Позволяет просматривать, редактировать информацию и удалить пользователя по его id

**URL** : `/luch/user/<int:pk>//`

**Method** : `GET`, `PUT` , `PATCH`, `DELETE`

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

````json
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
    }
]

# Регистрация нового пользователя

**URL** : `users/add/`

**Method** : `PUT` 

**Data constraints** : `{}`

**Success info** : HTTP 200 OK

**Content-Type** : application/json

**JSON** :
```json
{
    "id": "id",
    "password": "password",
    "last_login": "last_login",
    "is_superuser": "is_superuser",
    "username": "username",
    "first_name": "first_name",
    "last_name": "last_name",
    "is_staff": "is_staff",
    "is_active": "is_staff",
    "date_joined": "date",
    "email": "email",
    "groups": [],
    "user_permissions": []
}
```
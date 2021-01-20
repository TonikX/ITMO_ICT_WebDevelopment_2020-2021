# Показать профиль текущего пользователя

Выводит информацию о пользователе использующем данный токен для доступа к системе.

**URL** : `/auth/users/me`

**Method** : `GET`

**Auth required** : YES

## Success Responses

**Code** : `200 OK`

**Data** :

```json
{
    "is_teacher": false,
    "id": 1,
    "email": "klishin.nd16@gmail.com"
}
```
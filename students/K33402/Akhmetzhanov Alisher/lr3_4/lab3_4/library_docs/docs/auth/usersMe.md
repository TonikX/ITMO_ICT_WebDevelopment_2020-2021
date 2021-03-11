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
    "id": 1,
    "email": "ivanov@gmail.com",
    "is_librarian": false
}
```
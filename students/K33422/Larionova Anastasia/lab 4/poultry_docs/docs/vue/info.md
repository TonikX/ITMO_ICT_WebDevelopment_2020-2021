# Authorized user's info

Выводит информацию о зарегистрированном пользователе, позволяет редактировать поля в случае авторизации

**URL** : `/settings/`

**Methods** : `GET`, `PATCH`

## Success Responses

**Code** : `200 OK`

**Content** : `{}`

```json
    {
        "first_name": "Nastya",
        "last_name": "Larionova",
        "passport": "xx xxxxxx"
    }
```
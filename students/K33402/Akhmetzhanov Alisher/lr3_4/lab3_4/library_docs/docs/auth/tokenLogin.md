# Получить токен доступа

Позволяет получить токен доступа для последующей работы с системой.

**URL** : `/auth/token/login`

**Method** : `POST`	

**Auth required** : YES

## Success Responses

**Code** : `200 OK`

**Requied fiels** : email, password

```json
{
    "auth_token": "287dffa63d0b19b172c8290b559f72983bb51821"
}
```
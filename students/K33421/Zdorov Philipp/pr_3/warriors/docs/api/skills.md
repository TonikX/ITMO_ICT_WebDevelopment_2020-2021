# Показать всех воинов

Выводит информацию обо всех умения

**URL** : `skills/`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `application/json`

```json
{
    "Skills": [
        {
            "title": "swimming"
        },
        {
            "title": "fighting"
        }
    ]
}
```
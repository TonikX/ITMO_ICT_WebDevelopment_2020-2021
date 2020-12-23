# Эндпоинты


* ##Получить список всех услуг </br>
**URL** : `/api/service/`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
   "Services": [
    {
        "id": 1,
        "title": "Продвижение в FB",
        "price": 2000
    }
]
}
```


* ##Обновить заявку </br>


**URL** : `api/application/<int:pk>/update`

**Method** : `PUT`/`PATCH`

**Data constraints** : `{}`

**Content-Type** : application/json


* ##Обновить данные об услуге </br>


**URL** : `api/service/<int:pk>/update`

**Method** : `PUT`/`PATCH`

**Data constraints** : `{}`

**Content-Type** : application/json


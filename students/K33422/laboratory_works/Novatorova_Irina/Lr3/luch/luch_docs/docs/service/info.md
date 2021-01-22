# Просмотр/редактирование/удаление информации об услуге

**URL** : `/luch/service/<int:pk>/`

**Method** : `GET`, `PUT` , `PATCH`, `DELETE`

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "id": 1,
    "type_service": "polygraphy",
    "title": "визитка",
    "price": 10
}
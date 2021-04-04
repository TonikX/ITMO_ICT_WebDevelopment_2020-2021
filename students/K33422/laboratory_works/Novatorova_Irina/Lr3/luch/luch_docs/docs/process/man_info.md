# Просмотр/редактирование/удаление информации о процессе организации

**URL** : `/luch/manufactory/<int:pk>/`

**Method** : `GET`, `PUT` , `PATCH`, `DELETE`

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "id": 1,
    "quantity": 100,
    "total_price": 1000,
    "application": 1,
    "material": 2,
    "service": 1
}
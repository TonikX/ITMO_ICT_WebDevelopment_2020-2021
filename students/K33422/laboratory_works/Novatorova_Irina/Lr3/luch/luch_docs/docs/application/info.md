# Просмотр/редактирование/удаление информации о заявке

**URL** : `/luch/application/<int:pk>/`

**Method** : `GET`, `PUT` , `PATCH`, `DELETE`

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "id": 1,
    "date": "2021-01-20",
    "ad_product": "персональные визитки",
    "amount": "100 штук",
    "status": "n",
    "client": 1,
    "service": 1
}
# Просмотр/редактирование/удаление информации о клиенте

**URL** : `/luch/client/<int:pk>/`

**Method** : `GET`, `PUT` , `PATCH`, `DELETE`

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "id": 1,
    "client": "Валерия",
    "phone": "+79996543278",
    "email": "valeria@xgroup.com"
}
# Просмотр/редактирование/удаление информации о материале

**URL** : `/luch/material/<int:pk>/`

**Method** : `GET`, `PUT` , `PATCH`, `DELETE`

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "id": 1,
    "type_service": "paper",
    "title": "фотобумага Luxor",
    "desc": "для полиграфии"
}
# Просмотр/редактирование/удаление информации о сотруднике

**URL** : `/luch/worker/<int:pk>/`

**Method** : `GET`, `PUT` , `PATCH`, `DELETE`

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "id": 1,
    "name": "Кирилл",
    "phone": "+79112034567",
    "work_exp": 4
}
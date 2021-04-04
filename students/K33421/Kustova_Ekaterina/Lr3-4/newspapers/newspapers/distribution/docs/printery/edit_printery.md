# Редактирование данных о типографии

**URL** : `printeries/<int:pk>/edit/`

**Method** : `PUT` 

**Data constraints** : `{}`

**Success info** : HTTP 200 OK

**Content-Type** : application/json

**JSON** :
```json
{
    "id": "id",
    "printery_name": "printery_name",
    "printery_address": "printery_address",
    "opening_time": "00:00:00",
    "closing_time": "00:00:00"
}
```
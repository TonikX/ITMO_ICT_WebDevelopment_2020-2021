# Редактирование данных о партии газет

**URL** : `parties/<int:pk>/edit/`

**Method** : `PUT` 

**Data constraints** : `{}`

**Success info** : HTTP 200 OK

**Content-Type** : application/json

**JSON** :
```json
{
    "id": "id",
    "party_number": "party_number",
    "amount_of_copies": "amount_of_copies",
    "newspapers_name": "newspapers_name"
}
```
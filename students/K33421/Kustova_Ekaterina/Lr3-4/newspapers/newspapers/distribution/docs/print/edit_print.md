# Редактирование данных о печати

**URL** : `prints/<int:pk>/edit/`

**Method** : `PUT` 

**Data constraints** : `{}`

**Success info** : HTTP 200 OK

**Content-Type** : application/json

**JSON** :
```json
{
    "id": "id",
    "print_id": "print_id",
    "print_amount":"print_amount",
    "printery_name":  "printery_name",
    "party_number": "party_number"
}
```
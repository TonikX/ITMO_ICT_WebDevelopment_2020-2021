# Редактирование отчёта о распределении газет


**URL** : `reports/<int:pk>/edit/`

**Method** : `PUT` 

**Data constraints** : `{}`

**Success info** : HTTP 200 OK

**Content-Type** : application/json

**JSON** :
```json
{
    "id": "id",
    "report_number": "report_number",
    "print_amount": "print_amount",
    "party_number": "party_number",
    "office_number": "office_number"
}
```

#  Просмотр приема у врача


**URL** : `/api/appointments/<int:id>`

**Method** : `GET`

**Content-Type** : application/json

**Response data** :
```json
{
    "id": 1,
    "doctor": {
        "id": 2,
        "first_name": "Сергей",
        "middle_name": null,
        "last_name": "Поляков",
        "specialty": "Терапевт"
    },
    "cabinet": {
        "id": 1,
        "number": 111
    },
    "patient": 2,
    "finish_time": "2020-02-03T16:40:00Z",
    "start_time": "2020-02-03T15:40:00Z",
    "type": "Консультация - 1000p",
    "diagnosis": "",
    "health_status": "",
    "recommendations": "",
    "payed": false,
    "form_of_payment": "Банковская карта"
}
```

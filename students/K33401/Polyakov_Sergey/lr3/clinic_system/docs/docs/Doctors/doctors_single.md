#  Просмотр одного врача


**URL** : `/api/doctors/<int:id>/`

**Method** : `GET`

**Content-Type** : application/json

**Response data** :
```json
{
    "Doctor": {
        "id": 2,
        "first_name": "Сергей",
        "middle_name": null,
        "last_name": "Поляков",
        "specialty": "Терапевт",
        "education": "Университет им. Мечникова",
        "date_of_birth": "2000-01-01",
        "start_work_date": "2021-04-09",
        "finish_work_date": null,
        "contract_number": null
    },
    "Timetable": {
        "пн": {
            "cabinet": {
                "id": 1,
                "number": 111
            }
        },
        "вт": {
            "cabinet": {
                "id": 1,
                "number": 111
            }
        },
        "ср": {
            "cabinet": {
                "number": null
            }
        },
        "чт": {
            "cabinet": {
                "id": 1,
                "number": 111
            }
        },
        "пт": {
            "cabinet": {
                "number": null
            }
        },
        "сб": {
            "cabinet": {
                "id": 1,
                "number": 111
            }
        },
        "вс": {
            "cabinet": {
                "number": null
            }
        }
    }
}
```

# Приём у врача

Информация обо всех приёмах врача в журнале

## Cписок всех записей в журнале приёмов

**URL** : `/api/meeting/`

**Method** : `GET`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "id": 1,
        "date_meet": "2021-01-20",
        "time_meet": "14:00:00",
        "status": "Полное выздоровление",
        "price_status": true,
        "id_patient": 5,
        "id_doctor": 1,
        "id_price": 2
    }
]
```
## Добавить запись о приёме

**URL** : `/api/meeting/create`

**Method** : `POST`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "id": 3,
    "date_meet": "2021-01-03",
    "time_meet": "16:00:00",
    "status": "Полное выздоровление",
    "price_status": false,
    "id_patient": 4,
    "id_doctor": 4,
    "id_price": 5
}
```

## Просмотр, изменение и удаление записей о приёме

**URL** : `api/meeting/<int:pk>/`

**Method** : `GET`, `PUT`, `DELETE`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "id": 3,
    "date_meet": "2021-01-03",
    "time_meet": "16:00:00",
    "status": "Полное выздоровление",
    "price_status": true,
    "id_patient": 4,
    "id_doctor": 4,
    "id_price": 5
}
```

## Детальный информация о приёме

**URL** : `api/meeting/detail/`

**Method** : `GET`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "id": 1,
        "id_patient": {
            "id": 5,
            "fio": "Хазына Лариса Ивановна",
            "birthdate": "1951-10-24",
            "phone": "+79214567777",
            "passport": "7890123456"
        },
        "id_doctor": {
            "username": "admin",
            "fio": "Смоленская Татьяна Дмитриевна",
            "speciality": "",
            "education": "",
            "work_years": 19
        },
        "id_price": {
            "id": 2,
            "name": "Диагностика",
            "price": 1400
        },
        "date_meet": "2021-01-20",
        "time_meet": "14:00:00",
        "status": "Полное выздоровление",
        "price_status": true
    }
]
```
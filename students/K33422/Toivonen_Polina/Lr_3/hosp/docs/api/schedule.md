# График работы

Информация об эндпоинтах, связанных с расписанием работы врача в конкретном кабинете

## Cписок всех графиков

**URL** : `/api/schedule/`

**Method** : `GET`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "id": 1,
        "id_doctor": {
            "username": "admin",
            "fio": "Смоленская Татьяна Дмитриевна",
            "speciality": "",
            "education": "",
            "work_years": 19
        },
        "number_cabinet": {
            "number": 1,
            "owner": "Калмык Байгур Нурыевич",
            "phone": "+79218765432"
        },
        "start_time": "10:00:00",
        "end_time": "20:00:00",
        "day": "С понедельника по пятницу"
    },
    {
        "id": 3,
        "id_doctor": {
            "username": "admin3",
            "fio": "Леонидов Валерий Павлович",
            "speciality": "Уролог",
            "education": "VSH",
            "work_years": 19
        },
        "number_cabinet": {
            "number": 2,
            "owner": "Петров Алексей Гринович",
            "phone": "+79117635567"
        },
        "start_time": "08:30:00",
        "end_time": "13:00:00",
        "day": "С понедельника по субботу"
    }
]
```
## Добавить новый график

**URL** : `/api/schedule/create`

**Method** : `POST`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "id_doctor": 4,
    "number_cabinet": 2,
    "start_time": "08:30:00",
    "end_time": "13:00:00",
    "day": "С понедельника по пятницу"
}
```
## Просмотр, изменение и удаление графика

**URL** : `api/schedule/<int:pk>/`

**Method** : `GET`, `PUT`, `DELETE`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "id_doctor": 4,
    "number_cabinet": 2,
    "start_time": "08:30:00",
    "end_time": "13:30:00",
    "day": "С понедельника по субботу"
}
```
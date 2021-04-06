# Врачи

Информация об эндпоинтах, связанных с врачами клиники

## Cписок всех работников клиники

**URL** : `/api/doctor/`

**Method** : `GET`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "username": "admin",
        "fio": "Тойвонен Полина Денисовна",
        "speciality": "",
        "education": "",
        "work_years": 10
    },
    {
        "username": "admin3",
        "fio": "Леонидов Валерий Павлович",
        "speciality": "Стоматолог",
        "education": "MDI",
        "work_years": 6
    },
]
```
## Добавить нового врача

**URL** : `/api/doctor/create`

**Method** : `POST`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "username": "admin4",
    "fio": "Павлов Виктор Деканович",
    "speciality": "ЛОР",
    "education": "VSH",
    "work_years": 3
}
```

## Просмотр, изменение и удаление врача

**URL** : `api/doctor/<int:pk>/`

**Method** : `GET`, `PUT`, `DELETE`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "username": "admin4",
    "fio": "Павлов Виктор Деканович",
    "speciality": "ЛОР",
    "education": "VSH",
    "work_years": 4
}
```
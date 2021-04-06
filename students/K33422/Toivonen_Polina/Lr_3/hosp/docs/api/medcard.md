# Медицинская книжка

Информация об эндпоинтах, связанных с медкартой пациента

## Cписок всех записей в медкарте

**URL** : `/api/medcard/`

**Method** : `GET`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "id": 1,
        "start_date": "2021-03-09",
        "status": "В активной форме",
        "id_patient": {
            "id": 3,
            "fio": "Михайлов Станислав Вальерьянович",
            "birthdate": "1989-12-02",
            "phone": "+79217757557",
            "passport": "3424342453"
        },
        "id_diagnosis": {
            "id": 2,
            "name": "Хронический танзилит"
        }
    }
]
```
## Добавить запись в медкарту

**URL** : `/api/medcard/create`

**Method** : `POST`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "id_patient": 4,
    "id_diagnosis": 4,
    "start_date": "2021-02-09",
    "status": "Слабая форма"
}
```
## Просмотр, изменение и удаление записей медкарты

**URL** : `api/medcard/<int:pk>/`

**Method** : `GET`, `PUT`, `DELETE`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "id": 5,
    "start_date": "2021-03-01",
    "status": "Полное выздоровление",
    "id_patient": 4,
    "id_diagnosis": 4
}
```
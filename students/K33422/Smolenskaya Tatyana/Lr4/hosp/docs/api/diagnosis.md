# Диагнозы

Информация об эндпоинтах, связанных с диагнозами

## Cписок всех диагнозов

**URL** : `/api/diagnosis/`

**Method** : `GET`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "id": 1,
        "name": "Синусит"
    },
    {
        "id": 2,
        "name": "Хронический танзилит"
    },
    {
        "id": 3,
        "name": "Коронавирус"
    },
    {
        "id": 4,
        "name": "Кишечная палочка"
    },
    {
        "id": 5,
        "name": "Пневмония"
    }
]
```
## Добавить новый диагноз

**URL** : `/api/diagnosis/create`

**Method** : `POST`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "name": "Расстройство желудка"
}
```
## Просмотр, изменение и удаление диагноза

**URL** : `api/diagnosis/<int:pk>/`

**Method** : `GET`, `PUT`, `DELETE`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "id": 6,
    "name": "Излишняя кислотность желудка"
}
```
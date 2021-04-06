# Прейскурант

Информация об эндпоинтах, связанных с рассценками на предлагаемые услуги

## Cписок всех услуг

**URL** : `/api/price/`

**Method** : `GET`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "id": 1,
        "name": "Первичный осмотр",
        "price": 1600
    },
    {
        "id": 2,
        "name": "Диагностика",
        "price": 1400
    },
    {
        "id": 3,
        "name": "Анализ крови",
        "price": 1000
    },
    {
        "id": 5,
        "name": "Справка",
        "price": 700
    }
]
```
## Добавить новую услугу

**URL** : `/api/price/create`

**Method** : `POST`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "name": "Анализ мочи",
    "price": 400
}

```
## Просмотр, изменение и удаление услуги

**URL** : `api/price/<int:pk>/`

**Method** : `GET`, `PUT`, `DELETE`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "id": 6,
    "name": "Анализ мочи",
    "price": 450
}
```
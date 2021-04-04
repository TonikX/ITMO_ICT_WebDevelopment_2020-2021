# Список услуг

**URL** : `/luch/service/list/`

**Method** : `GET`

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "id": 1,
        "type_service": "polygraphy",
        "title": "визитка",
        "price": 10
    },
    {
        "id": 2,
        "type_service": "polygraphy",
        "title": "листовка",
        "price": 25
    },
    {
        "id": 3,
        "type_service": "polygraphy",
        "title": "календарь",
        "price": 100
    },
    {
        "id": 4,
        "type_service": "media ads",
        "title": "реклама на развороте журнала",
        "price": 5000
    },
    {
        "id": 5,
        "type_service": "transport ads",
        "title": "реклама в метро S",
        "price": 5000
    },
    {
        "id": 6,
        "type_service": "transport ads",
        "title": "реклама в метро М",
        "price": 7000
    },
    {
        "id": 7,
        "type_service": "transport ads",
        "title": "реклама в метро L",
        "price": 10000
    }
]
# Список выполненных (выполняемых) работ 
Выводит список работ с указанием заявки, материала и услуги

**URL** : `/luch/manufactory/list/`

**Method** : `GET`

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "id": 1,
        "application": {
            "id": 1,
            "date": "2021-01-20",
            "ad_product": "персональные визитки",
            "amount": "100 штук",
            "status": "n",
            "client": 1,
            "service": 1
        },
        "material": {
            "id": 2,
            "type_service": "paper",
            "title": "самоклеящаяся бумага Finn",
            "desc": "высшего качества"
        },
        "service": {
            "id": 1,
            "type_service": "polygraphy",
            "title": "визитка",
            "price": 10
        },
        "quantity": 100,
        "total_price": 1000
    },
    {
        "id": 2,
        "application": {
            "id": 2,
            "date": "2020-12-23",
            "ad_product": "календари с корпоративной символикой",
            "amount": "50 штук",
            "status": "p",
            "client": 2,
            "service": 3
        },
        "material": {
            "id": 1,
            "type_service": "paper",
            "title": "фотобумага Luxor",
            "desc": "для полиграфии"
        },
        "service": {
            "id": 3,
            "type_service": "polygraphy",
            "title": "календарь",
            "price": 100
        },
        "quantity": 50,
        "total_price": 5000
    }
]
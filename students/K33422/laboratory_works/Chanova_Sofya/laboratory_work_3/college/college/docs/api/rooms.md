
# Кабинеты

Информация об эндпоинтах, связанных с учебными кабнетами колледжа.

## Cписок всех кабинетов

**URL** : `/college/rooms/`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "id": 2,
        "subject_theme": "chemistry lab",
        "room_number": 1,
        "seats_quantity": 30
    },
    {
        "id": 5,
        "subject_theme": "physics lab",
        "room_number": 2,
        "seats_quantity": 30
    }
]
```
## Добавить кабинет

**URL** : `/college/rooms/add`

**Method** : `POST`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "room_number": 10,
    "seats_quantity": 150,
    "subject_theme": "h"
}
```

## Просмотр, изменение и удаление кабинета

**URL** : `college/rooms/<int:room_number>/`

**Method** : `POST`, `GET`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "id": 7,
    "subject_theme": "hall",
    "room_number": 10,
    "seats_quantity": 150
}
```


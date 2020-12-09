
# Расписание

Информация об эндпоинтах, связанных с расписание.

## Cписок всех записей в расписании

**URL** : `/college/schedule/`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "id": 1,
        "weekday": "Monday",
        "time": "8:20",
        "room_number": "1",
        "group_number": "101",
        "teacher": "Boris Popov",
        "subject": "Chemistry"
    },
    {
        "id": 2,
        "weekday": "Friday",
        "time": "8:20",
        "room_number": "1",
        "group_number": "101",
        "teacher": "Boris Popov",
        "subject": "Chemistry"
    }
]
```
## Добавить запись в расписание

**URL** : `/college/schedule/add`

**Method** : `POST`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "weekday": "2",
    "time": "4",
    "room_number": 5,
    "group_number": 1,
    "teacher": 6,
    "subject": 4
}ы
```

## Просмотр, изменение и удаление кабинета

**URL** : `college/schedule/<int:pk>/`

**Method** : `POST`, `GET`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "id": 4,
    "weekday": "Wednesday",
    "time": "15:20",
    "room_number": "2",
    "group_number": "101",
    "teacher": "Valeria Pavlienko",
    "subject": "Sociology"
}
```
## Просмотр расписания авторизированного студента или преподавателя

Только для авторизированных пользователей

**URL** : `college/schedule/mine`

**Method** : `POST`, `GET`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "id": 1,
        "weekday": "Monday",
        "time": "8:20",
        "room_number": "1",
        "group_number": "101",
        "teacher": "Boris Popov",
        "subject": "Chemistry"
    },
    {
        "id": 2,
        "weekday": "Friday",
        "time": "8:20",
        "room_number": "1",
        "group_number": "101",
        "teacher": "Boris Popov",
        "subject": "Chemistry"
    },
    {
        "id": 3,
        "weekday": "Tuesday",
        "time": "10:00",
        "room_number": "3",
        "group_number": "101",
        "teacher": "Valeria Pavlienko",
        "subject": "Sociology"
    }
]
```


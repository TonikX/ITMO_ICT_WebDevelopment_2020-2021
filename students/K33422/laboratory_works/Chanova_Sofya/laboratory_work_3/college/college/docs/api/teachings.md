
# Преподавания

Информация об эндпоинтах, связанных с преподаваниями - связями учителей с предметами, которые они ведут.

## Cписок всех преподаваний

**URL** : `/college/teachings/`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "id": 5,
        "teacher": "Boris Popov",
        "subject": "Chemistry"
    },
    {
        "id": 6,
        "teacher": "Valeria Pavlienko",
        "subject": "Sociology"
    }
]
```
## Добавить преподавание

**URL** : `/college/teachings/add`

**Method** : `POST`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "teacher": 6,
    "subject": 3
}
```

## Просмотр, изменение и удаление преподавания

**URL** : `college/teachings/<int:pk>/`

**Method** : `POST`, `GET`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "id": 7,
    "teacher": "Valeria Pavlienko",
    "subject": "Philosophy"
}
```



# Предметы

Информация об эндпоинтах, связанных с учебными дисциплинами.

## Cписок всех предметов

**URL** : `/college/subjects/`

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
        "control_type": "exam",
        "subject_name": "Chemistry",
        "academic_hours": 36,
        "description": null
    },
    {
        "id": 2,
        "control_type": "exam",
        "subject_name": "Biology",
        "academic_hours": 36,
        "description": ""
    }
]
```
## Добавить предмет

**URL** : `/college/subjects/add`

**Method** : `POST`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "subject_name": "Philosophy",
    "control_type": "e",
    "academic_hours": 36,
    "description": ""
}
```

## Просмотр, изменение и удаление предмета

**URL** : `college/subjects/<int:pk>/`

**Method** : `POST`, `GET`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "id": 5,
    "control_type": "exam",
    "subject_name": "Philosophy",
    "academic_hours": 36,
    "description": ""
}
```


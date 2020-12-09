
# Группы

Информация об эндпоинтах, связанных с учебными группами.

## Cписок всех групп

**URL** : `/college/groups/`

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
        "group_number": "101",
        "course_number": 1,
        "department": "Department of Chemistry"
    },
    {
        "id": 2,
        "group_number": "102",
        "course_number": 1,
        "department": "Department of Biology"
    }
]
```
## Добавить группу

**URL** : `/college/groups/add`

**Method** : `POST`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "group_number": "201",
    "course_number": 2,
    "department": "Department of Chemistry"
}
```

## Просмотр, изменение и удаление группы

**URL** : `college/groups/<int:pk>/`

**Method** : `POST`, `GET`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "id": 1,
    "group_number": "101",
    "course_number": 1,
    "department": "Department of Chemistry"
}
```


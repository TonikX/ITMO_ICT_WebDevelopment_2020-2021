
# Оценки

Информация об эндпоинтах, связанных с оценками студента за семестр.

## Cписок всех оценок

**URL** : `/college/grades/`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "student": "Lilith Hell",
        "subject": "Chemistry",
        "grade": "F",
        "graded_by": "Boris Popov"
    },
    {
        "student": "Lisa Orange",
        "subject": "Chemistry",
        "grade": "B",
        "graded_by": "Boris Popov"
    }
]
```
## Добавить оценку

**URL** : `/college/grades/add`

**Method** : `POST`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "student": 5,
    "teaching": 6,
    "grade": "A"
}
```

## Просмотр, изменение и удаление оценки

**URL** : `college/grades/<int:pk>/`

**Method** : `POST`, `GET`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "student": "Lilith Hell",
    "subject": "Chemistry",
    "grade": "F",
    "graded_by": "Boris Popov"
}
```


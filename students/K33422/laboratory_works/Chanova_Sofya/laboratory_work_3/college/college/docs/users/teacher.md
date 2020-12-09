# Пользователь-преподаватель

Преподаватель имеет возможность просматривать, добавлять, изменять и удалять информацию об оценках, просматривать информацию о группах и расписании.

## Поля профиля преподавателя:
- Username
- Роль ('t' - 'teacher')
- Имя
- Фамилия
- Email 

## Cписок всех преподавателей

**URL** : `/college/teachers/`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "username": "bobik",
        "role": "teacher",
        "first_name": "Boris",
        "last_name": "Popov",
        "email": "bobik@mail.ru",
        "teacher_qualification": "Chemistry teacher"
    },
    {
        "username": "lera",
        "role": "teacher",
        "first_name": "Valeria",
        "last_name": "Pavlienko",
        "email": "lera@mail.ru",
        "teacher_qualification": "Sociology teacher"
    }
]
```

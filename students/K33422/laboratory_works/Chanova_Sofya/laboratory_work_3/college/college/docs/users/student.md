# Пользователь-студент

Студент имеет возможность просматривать информацию по группам, свое расписание и список предметов.

## Поля профиля студента:
- Username
- Роль ('s' - 'student')
- Имя
- Фамилия
- Email 
- Учебная группа
- Семестровые оценки

## Cписок всех студентов

**URL** : `/college/students/`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "username": "lisa",
        "role": "student",
        "first_name": "Lisa",
        "last_name": "Orange",
        "email": "lisa@mail.ru",
        "student_group": "101"
    },
    {
        "username": "lilith",
        "role": "student",
        "first_name": "Lilith",
        "last_name": "Hell",
        "email": "lilith7@gmail.com",
        "student_group": "101"
    }
]
```


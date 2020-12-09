# Пользователь-диспетчер

Диспетчер имеет возможность просматривать, добавлять, изменять и удалять информацию о расписании.

## Поля профиля диспетчера:
- Username
- Роль ('d' - 'dispatcher')
- Имя
- Фамилия
- Email 

## Cписок всех диспетчеров

Можно посмотреть в списке персонала, куда входят администраторы и диспетчеры

**URL** : `/college/staff/`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "username": "spiritofsofya",
        "role": "admin",
        "first_name": "Sofya",
        "last_name": "Chanova",
        "email": "chanovas@outlook.com"
    },
    {
        "username": "roman",
        "role": "dispatcher",
        "first_name": "Roman",
        "last_name": "Romanenko",
        "email": "roman@mail.ru"
    }
]
```


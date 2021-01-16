# List Review

Выводит информацию о всех ревью пользователя

**URL** : `reviews/`

**Methods** : `GET`

**Data constraints** : `{}`

**Generics type** : `ListAPIView`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
  {
    "id": 1,
    "author": {
      "username": "asssalad138",
      "first_name": "Иван",
      "last_name": "Шкикавый",
      "email": "asssalad138@yandex.ru"
    },
    "creation": {
      "id": 1,
      "name": "Капитанская дочка",
      "description": "исторический роман Александра Пушкина, действие которого происходит во время восстания Емельяна Пугачёва. Впервые опубликован без указания имени автора в 4-й книжке журнала «Современник», поступившей в продажу в последней декаде 1836 года.",
      "type": "Литература",
      "creator": 1
    },
    "text": "Это было великолепно",
    "rating": 5
  }
]
```
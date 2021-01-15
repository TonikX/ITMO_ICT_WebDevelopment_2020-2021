# Описание пользователя

Возможности пользователя:

* просматривать опросы
* создавать и изменять опрос
* проходить опросы

Структура пользователя:
```json
{
    "id": 0,
    "username": "string",
    "name": "string",
    "email": "user@example.com",
    "date_of_birth": "2020-12-06"
  }
```

Методы для работы с пользователем:

* GET
/user/
user_list

* POST
/user/
user_create

* GET
/user/{id}/
user_read

* PUT
/user/{id}/
user_update

* DELETE
/user/{id}/
user_delete


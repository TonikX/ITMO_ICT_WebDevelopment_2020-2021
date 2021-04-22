# Регистрация

Отправка POST запроса с корректными данными по адресу `/auth/users/` позволит создать нового пользователя в базе данных.

Стоит обратить внимание, что в списке обязательных аргументов являются:

- username (must be unique)
- email
- password (has additional requirements, has to be **strong**)
- first_name
- last_name

## Success

```
{
    "email": "poko@mail.ru",
    "username": "poko",
    "id": 6
}
```

## Error

```
{
    "username": [
        "A user with that username already exists."
    ]
}
```

# Менеджер отелей

Запуск

`python manage.py runserver`

`mkdocs serve`

## Эндпоинты

### Авторизация

`/auth/token/login/`

```JSON
{
    "password": "enter the password here",
    "username": "enter the username here"
}
```

#### Результат

```JSON
HTTP 200 OK
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "auth_token": "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}
```

### Регистрация

`/auth/users`

```JSON
{
    "first_name": "example_name",
    "last_name": "example_surname",
    "email": "example@mail.ru",
    "username": "example",
    "password": "password12345password"
}
```

#### Результат

```JSON
HTTP 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "first_name": "example_name",
    "last_name": "example_surname",
    "email": "example@mail.ru",
    "username": "example",
    "id": 3
}
```
### Запросы
#### Get request

`/rooms/list/` - Получить информацию о существующих комнатах

`/rooms/info/{pk}/` - Получить информацию о конкретной комнате

`/staff/list/` - Получить информацию о существующем персонале

`/staff/info/{pk}/` - Получить информацию о конкретном персонале

`/guests/list/` - Получить информацию о гостях

`/guests/info/{pk}/` - Получить информацию о конкретном госте

`/cleanings/list/` - Получить информацию об уборках

`/cleanings/info/{pk}/` - Получить информацию о конкретной уборке

`/users/info/{pk}/` - Получить информацию о конкретном зарегистрированном пользователе

#### Post request

`/rooms/add/` - Добавить комнату

`/staff/add/` - Добавить члена персонала

`/guests/add/` - Добавить гостя

`/cleanings/add/` - Добавить уборку

`/users/add/` - Добавить пользователя

#### Put/Patch request

`/rooms/info/{pk}/` - Изменить информацию о комнате

`/staff/info/{pk}/` - Изменить информацию о члене персонала

`/guests/info/{pk}/` - Изменить информацию о госте

`/cleanings/info/{pk}/` - Изменить информацию об уборке

`/users/info/{pk}/` - Изменить информацию о зарегистрированном пользователе
#### Delete request

`/rooms/info/{pk}/` - Удалить комнату

`/staff/info/{pk}/` - Удалить члена персонала

`/guests/info/{pk}/` - Удалить гостя

`/cleanings/info/{pk}/` - Удалить уборку

`/users/info/{pk}/` - Удалить пользователя
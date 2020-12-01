# LibraryManage
Создавайте свою базу данных для библиотек с удобным API
### Get started
```systemctl start postgresql```

```python manage.py runserver 8005```

```mkdocs serve```

## Available endpoints

###Authentication request
* `/auth/token/login/` - Авторизация
#####Пример POST:
```
{
    "password": "root",
    "username": "root"
}
```
#####Результат:

```
HTTP 200 OK
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "auth_token": "91d3db7855aef7179f7307dd79fcaf66a654f9db"
}
```

* `/auth/token/logout/` - Выход
#####Пример POST:
```
{}
```
#####Результат:
```
HTTP 204 No Content
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept
```

* `/auth/token/logout/` - Регистрация
#####Пример POST:
```
{
    "email": "example@gmail.com",
    "username": "example",
    "password": "exampleexample"
}
```
#####Результат:
```
HTTP 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "email": "example@gmail.com",
    "username": "example",
    "id": 9
}
```

###Get request
* `/api/books/{pk}` - Получить полный список книг, при не пустом `pk` возвращает конкретное значение
* `/api/readers/{pk}` - Получить полный список читателей, при не пустом `pk` возвращает конкретное значение
* `/api/instancesOfBook/{pk}` - Получить полный список экземпляров книг, при не пустом `pk` возвращает конкретное значение
* `/api/issuingAInstances/{pk}` - Получить полный список выданных экземпляров, при не пустом `pk` возвращает конкретное значение
* `/api/readingRoom/{pk}` - Получить полный список читательских залов, при не пустом `pk` возвращает конкретное значение
* `/api/instanceOfBookInReadingRoom/{pk}` - Получить полный список экземпляров книг в читательских залах, при не пустом `pk` возвращает конкретное значение
* `/api/registers/{pk}` - Получить полный список регистраций читателей, при не пустом `pk` возвращает конкретное значение

###Post request
* `/api/books/` - Добавить запись
* `/api/readers/` - Добавить запись
* `/api/instancesOfBook/` - Добавить запись
* `/api/issuingAInstances/` - Добавить запись
* `/api/readingRoom/` - Добавить запись
* `/api/instanceOfBookInReadingRoom/` - Добавить запись
* `/api/registers/` - Добавить запись


###Put request
* `/api/books/` - Добавить запись
* `/api/readers/` - Добавить запись
* `/api/instancesOfBook/` - Добавить запись
* `/api/issuingAInstances/` - Добавить запись
* `/api/readingRoom/` - Добавить запись
* `/api/instanceOfBookInReadingRoom/` - Добавить запись
* `/api/registers/` - Добавить запись


###Post request
* `/api/books/{pk}` - Обновить запись с `pk = id`
* `/api/readers/{pk}` - Обновить запись с `pk = id`
* `/api/instancesOfBook/{pk}` - Обновить запись с `pk = id`
* `/api/issuingAInstances/{pk}` - Обновить запись с `pk = id`
* `/api/readingRoom/{pk}` - Обновить запись с `pk = id`
* `/api/instanceOfBookInReadingRoom/{pk}` - Обновить запись с `pk = id`
* `/api/registers/{pk}` - Обновить запись с `pk = id`


###Delete request
* `/api/books/{pk}` - Удалить запись с `pk = id`
* `/api/readers/{pk}` - Удалить запись с `pk = id`
* `/api/instancesOfBook/{pk}` - Удалить запись с `pk = id`
* `/api/issuingAInstances/{pk}` - Удалить запись с `pk = id`
* `/api/readingRoom/{pk}` - Удалить запись с `pk = id`
* `/api/instanceOfBookInReadingRoom/{pk}` - Удалить запись с `pk = id`
* `/api/registers/{pk}` - Удалить запись с `pk = id`
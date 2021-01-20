# Пиццерия

Зарегистрированный пользователь может создавать (формировать), изменять и удалять заказы.

Все сделанные заказы можно увидеть по POST запросу:

**URL** : `/api/orders/`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : IsOwner

**Code** : `200 OK`

**Content** :
```json
{
    "id": 1,
    "pizzas": [
      {
        "id": 1,
        "name": "Peperoni",
        "price": 300
      },
      {
        "id": 3,
        "name": "Carbanara",
        "price": 350
      }
    ]
  },
  {
    "id": 2,
    "pizzas": [
      {
        "id": 2,
        "name": "Margarita",
        "price": 200
      }
    ]
  }
```
<br>
Изменение информации о конкретной пицце по PATCH/PUT запросу:

**URL** : `pizzas/{id}/update/`

**Method** : `PATCH/PUT`

**Auth required** : YES

**Permissions required** : IsAdminUser

**Code** : `200 OK`

**Content** :
```json
{
  "id": 3,
  "name": "Carbanara",
  "price": 250
}
```
<br>
Получение информации о конкретной пицце получаем по GET запросу:

**URL** : `pizzas/{id}/`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : IsAuthenticated

**Code** : `200 OK`

**Content** :
```json
{
  "id": 2,
  "name": "Margarita",
  "price": 200
}
```
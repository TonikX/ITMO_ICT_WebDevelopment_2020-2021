### Список комнат

`rooms/list/`

#### Результат

```JSON
[
    {
        "number": 111,
        "type": "1",
        "price": 100,
        "floor": 1,
        "cleaners": [
            1
        ]
    },
    {
        "number": 222,
        "type": "2",
        "price": 200,
        "floor": 2,
        "cleaners": [
            2
        ]
    }
]
```

### Список персонала

`staff/list/`

#### Результат

```JSON
[
    {
        "id": 1,
        "passport_number": "0000",
        "first_name": "Ivan",
        "surname": "Ivanov",
        "patronymic": "Ivanovich",
        "from_location": "Moskow",
        "check_in_date": "2021-02-05",
        "check_out_date": "2021-02-07",
        "room": 111
    },
    {
        "id": 2,
        "passport_number": "1111",
        "first_name": "Vasya",
        "surname": "Pupkin",
        "patronymic": "Ivanovich",
        "from_location": "Omsk",
        "check_in_date": "2021-02-02",
        "check_out_date": "2021-02-04",
        "room": 222
    }
]
```

### Список уборок

`cleanings/list/`

#### Результат

```JSON
[
    {
        "id": 1,
        "date_time": "2021-02-07T18:46:29Z",
        "room": 111,
        "staff": 1
    },
    {
        "id": 2,
        "date_time": "2021-02-07T18:46:42Z",
        "room": 222,
        "staff": 2
    }
]
```

### Список гостей

`guests/list/`

#### Результат

```JSON
[
    {
        "id": 1,
        "passport_number": "0000",
        "first_name": "Ivan",
        "surname": "Ivanov",
        "patronymic": "Ivanovich",
        "from_location": "Moscow",
        "check_in_date": "2021-02-05",
        "check_out_date": "2021-02-07",
        "room": 111
    },
    {
        "id": 2,
        "passport_number": "1111",
        "first_name": "Vasya",
        "surname": "Pupkin",
        "patronymic": "Ivanovich",
        "from_location": "Omsk",
        "check_in_date": "2021-02-02",
        "check_out_date": "2021-02-04",
        "room": 222
    }
]
```

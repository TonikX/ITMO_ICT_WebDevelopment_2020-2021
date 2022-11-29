# Модели
###Room
```    
{
    "number": 101,
    "type": "1",
    "price": 3000,
    "floor": 1,
    "cleaners": [
        1,
        1
    ]
}
```

###Guest
```    
{
    "id": 1,
    "passport_number": "6920 234556",
    "name": "Liza",
    "surname": "Kotova",
    "middlename": "Sergeevna",
    "from_location": "Tomsk",
    "check_in_date": "2021-02-12",
    "room": 101
}
```

###Staff
```    
{
    "id": 1,
    "name": "Elena",
    "surname": "Simonova",
    "middlename": "Vitalievna"
}
```

###Cleaning
```    
{
    "id": 1,
    "date_time": "2021-02-12T12:00:00Z",
    "room": 101,
    "staff": 1
}
```


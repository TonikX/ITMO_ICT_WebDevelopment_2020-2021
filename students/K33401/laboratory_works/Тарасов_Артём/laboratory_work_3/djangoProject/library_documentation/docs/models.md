# Модели
###Book
```    
{
    "id": 1,
    "owner": 1,
    "author": "1",
    "name": "name",
    "year_of_pub": "2020-11-28",
    "section": null,
    "pressmark": null,
    "debit_date": "2020-11-28"
}
```

###Instance Of Book
```    
{
    "id": 123,
    "owner": 1,
    "status": true,
    "id_book": 123
}
```

###Reader
```    
{
    "id": 123,
    "owner": 1,
    "full_name": "Artyom",
    "passport_number": 13543,
    "birthday": "2020-11-13",
    "address": "Saint-Petersburg",
    "phone": 2147483647,
    "degree": "Middle",
    "graduate_degree": false,
    "books": [
        123
    ]
}
```



###Issuing A Instance
```    
{
    "id": 1,
    "owner": 1,
    "start_date": "2020-11-28",
    "return_date": "2020-11-13",
    "instance": 123,
    "reader": 123
}
```



###Reading Room
```
{
    "id": 1,
    "owner": 1,
    "name": "Name",
    "size": 1000
}
```

###Registers
```
{
    "id": 1,
    "owner": 1,
    "register_date": "2020-11-29",
    "update_date": "2020-11-29",
    "unregister_date": "2020-11-29",
    "id_reader": 123,
    "id_room": 1
}
```    

###Instance Of Book In Reading Room
```
    {
        "id": 1,
        "owner": 1,
        "count": 10,
        "id_instance": 123,
        "id_room": 1
    }
```    
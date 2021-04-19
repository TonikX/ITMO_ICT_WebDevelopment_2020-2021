# Посмотреть, отредактировать или удалить воина

Метод для изменения экземпляра воина:

**URL** : `/war/warrior/action/<int:pk>`

**Method** : `GET/PUT/PATCH/DELETE`

**Auth required** : None

**Permissions required** : None

**Body** : 
```json
{
  "profession": {
    "title": "string",
    "description": "string"
  },
  "skill": [
    {
      "title": "string"
    }
  ],
  "name": "string",
  "level": 0
}
```

**

## Success Responses

**Code** : `200 Success`

**Content** : `{}`

```json
{
    "race": "String",
    "name": "String",
    "level": "Number",
    "profession": {
        "title": "String",
        "description": "String"
    },
    "skill": [
        {
            "title": "String"
        }
    ]
}
```
    


# Создать воина

Метод для изменения экземпляра воина:

**URL** : `/war/warriors/<int:pk>`

**Method** : `PUT/PATCH`

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
    


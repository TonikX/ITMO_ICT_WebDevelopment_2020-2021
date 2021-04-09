# Создать воина

Метод для создания экземпляра воина:

**URL** : `/war/warrior/create`

**Method** : `POST`

**Auth required** : None

**Permissions required** : None

**Body** : 
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

**

## Success Responses

**Code** : `201 Created`

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
    


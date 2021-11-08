# Создать воина

Метод для создания экземпляра воина:

**URL** : `/api/warriors/create`

**Method** : `POST`

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

**Code** : `201 Created`

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
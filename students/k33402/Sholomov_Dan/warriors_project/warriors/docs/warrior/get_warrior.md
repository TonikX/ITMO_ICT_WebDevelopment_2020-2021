# Получить инфорацию о воине, профессии и его скиллах

Метод для получения информации о воине:

**URL** : `/war/warriors/`

**Method** : `GET`

**Auth required** : None

**Permissions required** : None

## Success Responses

**Code** : `200 Success`

**Content** : `{[]}`

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
    


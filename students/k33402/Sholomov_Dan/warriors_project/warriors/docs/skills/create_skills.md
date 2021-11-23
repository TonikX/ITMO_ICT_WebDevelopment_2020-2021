# Создать навык

Метод для создания экземпляра навыка:

**URL** : `/war/skills/create`

**Method** : `POST`

**Auth required** : None

**Permissions required** : None

**Body** : 
```json
{
  "skill": 
    {
      "title": "string"
    }
}
```

## Success Responses

**Code** : `201 Created`

**Content** : `{}`

```json
{
    "Success": "Skill 'title' created successfully."
}
```
    


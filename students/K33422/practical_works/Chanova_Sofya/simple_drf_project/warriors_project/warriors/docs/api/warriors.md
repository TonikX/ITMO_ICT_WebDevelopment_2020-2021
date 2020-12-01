
# show all warriors

displays all warriors' info

**URL** : `/api/warriors/`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

## success responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
   "Warriors": [
       {
           "id": 1,
           "race": "t",
           "name": "Lobster",
           "level": 0,
           "profession": null,
           "skill": []
       },
       {
           "id": 2,
           "race": "s",
           "name": "Shrimp",
           "level": 0,
           "profession": null,
           "skill": []
       }
   ]
}
```

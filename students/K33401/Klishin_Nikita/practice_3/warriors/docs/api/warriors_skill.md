# Показать воинов и их умения

Выводит список войнов и их умения

**URL** : `/api/warriors_skill/`

**Method** : `GET`

<!-- **Auth required** : YES -->

**Permissions required** : None

<!-- **Data constraints** : `{}` -->

## Success Responses

**Code** : `200 OK`

<!-- **Content** : `{[]}` -->

```json
{
	[
		{
        "id": 1,
        "skill": [
            {
                "id": 2,
                "title": "Water"
            }
        ],
        "race": "s",
        "name": "Student1",
        "level": 7,
        "profession": 1
    },
    {
        "id": 2,
        "skill": [
            {
                "id": 1,
                "title": "Fire"
            }
        ],
        "race": "d",
        "name": "Developer 1",
        "level": 7,
        "profession": 1
    }
]
}
```
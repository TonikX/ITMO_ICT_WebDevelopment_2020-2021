# Добавление нового материала

**URL** : `/luch/material/create/`

**Method** : `PUT`

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

views.py:
```json
class MaterialCreateAPIView(generics.CreateAPIView):
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()
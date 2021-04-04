# Добавление новой заявки

**URL** : `/luch/application/create/`

**Method** : `PUT`

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

views.py:
```json
class ApplicationCreateAPIView(generics.CreateAPIView):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()
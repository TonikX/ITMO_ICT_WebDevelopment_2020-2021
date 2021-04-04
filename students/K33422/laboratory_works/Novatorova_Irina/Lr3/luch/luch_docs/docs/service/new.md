# Добавление новой услуги

**URL** : `/luch/service/create/`

**Method** : `PUT`

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

views.py:
```json
class ServiceCreateAPIView(generics.CreateAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
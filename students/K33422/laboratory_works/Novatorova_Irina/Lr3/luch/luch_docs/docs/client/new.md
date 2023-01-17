# Добавление нового клиента

**URL** : `/luch/client/create/`

**Method** : `PUT`

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

views.py:
```json
class ClientCreateAPIView(generics.CreateAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

# Список заявок 
Выводит список заявок с указанием клиента и услуги c возможностью фильтрации по клиенту

**URL** : `/luch/application/list/`

**Method** : `GET`

**Data constraints** : `{}`

###С фильтрацией по клиенту (id клиента=1)
**URL** : `/luch/application/list?client=1/`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

views.py:

```json
class ApplicationNestedAPIView(generics.ListAPIView):
    serializer_class = ApplicationNestedSerializer

    def get_queryset(self):
        queryset = Application.objects.all()

        params = self.request.query_params

        client = params.get('client', None)

        if client:
            queryset = queryset.filter(client=client)

        return queryset

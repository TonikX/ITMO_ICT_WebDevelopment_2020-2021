# Добавление нового сотрудника

**URL** : `/luch/worker/create/`

**Method** : `PUT`

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

views.py:
```json
class WorkerCreateAPIView(generics.CreateAPIView):
    serializer_class = WorkerSerializer
    queryset = Worker.objects.all()
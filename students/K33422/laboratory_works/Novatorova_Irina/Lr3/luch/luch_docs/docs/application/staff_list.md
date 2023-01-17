# Служебный список заявок 
Выводит список заявок с указанием сотрудника и услуги c возможностью фильтрации по сотруднику

**URL** : `/luch/application_list/list/`

**Method** : `GET`

**Data constraints** : `{}`

###С фильтрацией по сотруднику (id сотрудника=1)
**URL** : `/luch/application_list/list?worker=1`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

views.py:

```json
class ApplicationListNestedAPIView(generics.ListAPIView):
    serializer_class = ApplicationListNestedSerializer

    def get_queryset(self):
        queryset = Application_list.objects.all()

        params = self.request.query_params

        worker = params.get('worker', None)

        if worker:
            queryset = queryset.filter(worker=worker)

        return queryset




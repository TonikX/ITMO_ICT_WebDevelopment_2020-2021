# Update/delete service

Позволяет обновлять или удалять информацию об обслуживании по id

**URL** : `/services/info/<int:pk>/`

**Methods** : `PUT` & `DELETE`

**Data constraints** : `{}`

**Generics type** : `RetrieveUpdateDestroyAPIView`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```python
class ServiceInfoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
```

```python
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"
```
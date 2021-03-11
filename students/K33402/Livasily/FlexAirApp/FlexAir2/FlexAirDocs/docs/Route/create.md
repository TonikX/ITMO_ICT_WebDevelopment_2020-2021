# Create route

Создает новый маршрут

# **URL** : `/Route/create/`

**Methods** : `PUT`

**Data constraints** : `{}`

**Generics type** : `CreateAPIView`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```python
class RouteCreateAPIView(generics.CreateAPIView):
    serializer_class = RouteSerializer
    queryset = Route.objects.all()
```

```python
class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = "__all__"
```


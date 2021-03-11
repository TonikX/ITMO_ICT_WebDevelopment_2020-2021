# Create Plan

Создает новый самолет

**URL** : `/Plan/create/`

**Methods** : `PUT`

**Data constraints** : `{}`

**Generics type** : `CreateAPIView`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```python
class PlaneCreateAPIView(generics.CreateAPIView):
    serializer_class = PlaneSerializer
    queryset = Plane.objects.all()
```

```python
class PlaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plane
        fields = "__all__"
```


# Create Airline

Создает новый аэропорт

**URL** : `/Hotel/create/`

**Methods** : `PUT`

**Data constraints** : `{}`

**Generics type** : `CreateAPIView`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```python
class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = "__all__"

```

```python
class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = HotelSerializer
```


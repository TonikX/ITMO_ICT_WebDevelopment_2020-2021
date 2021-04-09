# Create Place

Создает новое зарезервированное место

**URL** : `/place`

**Methods** : `PUT`

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

## Code

```python
class PlaceViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = Place.objects.all()
        num_flight = self.request.query_params.get('num_flight', None)
        passenger = self.request.query_params.get('passenger', None)
        if num_flight is not None:
            queryset = queryset.filter(num_flight=num_flight)
        elif passenger is not None:
            queryset = queryset.filter(passenger=passenger)
        return queryset

    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = PlaceSerializer
```

```python
class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = "__all__"
```


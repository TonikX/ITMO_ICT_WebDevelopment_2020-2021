# Create Flight

Создает новый рейс

**URL** : `/flight`

**Methods** : `PUT`

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

## Code

```python
class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = FlightSerializer
```

```python
class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = "__all__"
```


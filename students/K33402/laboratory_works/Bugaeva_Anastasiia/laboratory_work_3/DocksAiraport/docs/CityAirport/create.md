# Create CityAirport

Создает новый городы и его аэропорт

**URL** : `/cityAirport`

**Methods** : `PUT`

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

## Code

```python
class CityAirportViewSet(viewsets.ModelViewSet):
    queryset = CityAirport.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = CityAirportSerializer
```

```python
class CityAirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityAirport
        fields = "__all__"
```


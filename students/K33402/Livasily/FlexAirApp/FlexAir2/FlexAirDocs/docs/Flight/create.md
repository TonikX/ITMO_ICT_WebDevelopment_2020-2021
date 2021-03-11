# Create Flight

Создает новый рейс

**URL** : `/Flight/create/`

**Methods** : `PUT`

**Data constraints** : `{}`

**Generics type** : `CreateAPIView`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```python
class FlightCreateAPIView(generics.CreateAPIView):
    serializer_class = FlightSerializer
    queryset = Flight.objects.all()
```

```python
class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = "__all__"
```


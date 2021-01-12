# Create Arrival

Создает новый Перелетах

**URL** : `/Arrival/create/`

**Methods** : `PUT`

**Data constraints** : `{}`

**Generics type** : `CreateAPIView`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```python
class AirportsListAPIView(generics.ListAPIView):
    serializer_class = AiraportNestedSerializer
    queryset = Airport.objects.all()
```

```python
class ArrivalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arrival
        fields = "__all__"
```


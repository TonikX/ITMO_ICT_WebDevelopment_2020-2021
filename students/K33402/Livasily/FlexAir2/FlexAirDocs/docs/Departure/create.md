# Create Departure

Создает новый отлет

**URL** : `/Departure/create/`

**Methods** : `PUT`

**Data constraints** : `{}`

**Generics type** : `CreateAPIView`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```python
class DepartureCreateAPIView(generics.CreateAPIView):
    serializer_class = DepartureSerializer
    queryset = Departure.objects.all()

```

```python
class DepartureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departure
        fields = "__all__"
```


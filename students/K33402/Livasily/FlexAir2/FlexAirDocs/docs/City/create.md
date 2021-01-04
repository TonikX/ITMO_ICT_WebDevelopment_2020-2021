# Create City

Создает новый город

**URL** : `/City/create/`

**Methods** : `PUT`

**Data constraints** : `{}`

**Generics type** : `CreateAPIView`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```python
class CityCreateAPIView(generics.CreateAPIView):
    serializer_class = CityCreateSerializer
    queryset = City.objects.all()
```

```python
class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ["name"]
```


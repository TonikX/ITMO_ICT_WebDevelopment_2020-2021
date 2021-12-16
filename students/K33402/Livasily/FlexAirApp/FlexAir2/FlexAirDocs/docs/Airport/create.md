# Create Airaport

Создает новый аэропорт

**URL** : `/Airaport/create/`

**Methods** : `PUT`

**Data constraints** : `{}`

**Generics type** : `CreateAPIView`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```python
class AirportCreateAPIView(generics.CreateAPIView):
    serializer_class = AirportCreateSerializer
    queryset = Airport.objects.all()
```

```python
class AirportCreateSerializer(serializers.ModelSerializer):
    company = AirlineSerializer()

    class Meta:
        model = Airport
        fields = "__all__"

    def create(self, validated_data):
        airoport = Airport(**validated_data)
        airoport.save()
        return Airport(**validated_data)
```


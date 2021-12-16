# Create Airline

Создает новый аэропорт

**URL** : `/breeds/create/`

**Methods** : `PUT`

**Data constraints** : `{}`

**Generics type** : `CreateAPIView`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```python
class AirlineCreateAPIView(generics.CreateAPIView):
    serializer_class = AirlineSerializer
    queryset = Airline.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
```

```python
class AirlineSerializer(serializers.ModelSerializer):
    owner = serializers.CharField()

    class Meta:
        model = Airline
        fields = "__all__"

    def create(self, validated_data):
        airline = Airline(**validated_data)
        airline.save()
        return Airline(**validated_data)
```


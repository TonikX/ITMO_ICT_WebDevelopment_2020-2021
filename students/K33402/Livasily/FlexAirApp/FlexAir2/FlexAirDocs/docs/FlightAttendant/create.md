# Create FlightAttendant

Создает нового бортпроводника

**URL** : `/FlightAttendant/create/`

**Methods** : `PUT`

**Data constraints** : `{}`

**Generics type** : `CreateAPIView`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```python
class FlightAttendantCreateAPIView(generics.CreateAPIView):
    serializer_class = FlightAttendantSerializer
    queryset = FlightAttendant.objects.all()
```

```python
class FlightAttendantSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightAttendant
        fields = "__all__"
```


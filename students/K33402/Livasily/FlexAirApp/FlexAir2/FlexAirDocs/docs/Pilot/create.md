# Create Pilot

Создает новый пилотов

**URL** : `/FlightAttendant/create/`

**Methods** : `PUT`

**Data constraints** : `{}`

**Generics type** : `CreateAPIView`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```python
class PilotCreateAPIView(generics.CreateAPIView):
    serializer_class = PilotSerializer
    queryset = Pilot.objects.all()

```

```python
class PilotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pilot
        fields = "__all__"
```


# Create Airline

Создает новую Авиакомпанию

**URL** : `/airlines`

**Methods** : `PUT`

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

## Code

```python
class AirlinesViewSet(viewsets.ModelViewSet):
    queryset = Airlines.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = AirlinesSerializer
```

```python
class AirlinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airline
        fields = "__all__"
```


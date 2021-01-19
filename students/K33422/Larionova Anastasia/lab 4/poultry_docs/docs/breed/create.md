# Create breed

Создает новую породу

**URL** : `/breeds/create/`

**Methods** : `PUT`

**Data constraints** : `{}`

**Generics type** : `CreateAPIView`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```python
class BreedCreateAPIView(generics.CreateAPIView):
    serializer_class = BreedSerializer
    queryset = Breed.objects.all()
```

```python
class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = "__all__"
```
# Create cell

Создает новую клетку

**URL** : `/cells/create/`

**Methods** : `PUT`

**Data constraints** : `{}`

**Generics type** : `CreateAPIView`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```python
class CellCreateAPIView(generics.CreateAPIView):
    serializer_class = CellSerializer
    queryset = Cell.objects.all()
```

```python
class CellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cell
        fields = "__all__"
```
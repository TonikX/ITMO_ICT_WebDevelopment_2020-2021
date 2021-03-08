# Update/delete cell

Позволяет обновлять или удалять информацию о клетке по id

**URL** : `/cells/info/<int:pk>/`

**Methods** : `PUT` & `DELETE`

**Data constraints** : `{}`

**Generics type** : `RetrieveUpdateDestroyAPIView`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```python
class CellInfoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cell.objects.all()
    serializer_class = CellSerializer
```

```python
class CellRelatedSerializer(serializers.ModelSerializer):
    row = serializers.StringRelatedField(read_only=True)
    tsekh = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Cell
        fields = "__all__"
```
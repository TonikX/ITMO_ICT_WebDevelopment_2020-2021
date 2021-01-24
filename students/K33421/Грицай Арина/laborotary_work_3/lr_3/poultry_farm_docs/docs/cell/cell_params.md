# List info of all cells

**URL** : `/cells/list/`

**Method** : `GET`

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "id": 1,
        "cell": 10,
        "row": 10,
        "tsekh": 1
    },
    {
        "id": 2,
        "cell": 12,
        "row": 12,
        "tsekh": 2
    },
    {
        "id": 3,
        "cell": 13,
        "row": 13,
        "tsekh": 3
    },
]
```

# Update/delete cell on id

**URL** : `/cells/info/<int:pk>/`

**Methods** : `PUT` & `DELETE`

**Data constraints** : `{}`

**Generics type** : `RetrieveUpdateDestroyAPIView`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```python
class CellChangeInfoAPIView(generics.RetrieveUpdateDestroyAPIView):
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

# Add cell

**URL** : `/cells/create/`

**Methods** : `PUT`

**Data constraints** : `{}`

**Generics type** : `CreateAPIView`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```python
class CellAddAPIView(generics.CreateAPIView):
    serializer_class = CellSerializer
    queryset = Cell.objects.all()
```

```python
class CellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cell
        fields = "__all__"
```
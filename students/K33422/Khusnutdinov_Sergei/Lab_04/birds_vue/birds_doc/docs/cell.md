# Create cell

Allows to create a new cell

**URL** : `/cells/create/`

**Methods** : `PUT`

**Data constraints** : `{}`

**Generics type** : `CreateAPIView`

Success Responses

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


# Update/delete cell

Allows to update or delete cell info

**URL** : `/cells/info/<int:pk>/`

**Methods** : `PUT` & `DELETE`

**Data constraints** : `{}`

**Generics type** : `RetrieveUpdateDestroyAPIView`

Success Responses

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


# List of cells

Allows to see the whole info about cells

**URL** : `/cells/list/`

**Method** : `GET`

**Data constraints** : `{}`

Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "id": 1,
        "cell": 1,
        "row": 1,
        "tsekh": 1
    },
    {
        "id": 2,
        "cell": 1,
        "row": 1,
        "tsekh": 2
    }
]
```
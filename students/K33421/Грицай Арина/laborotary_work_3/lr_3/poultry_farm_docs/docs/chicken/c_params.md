# List of all chickens

**URL** : `/chickens/list/`

**Method** : `GET`

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "id": 1,
        "breed": "Broiler",
        "cell": "10",
        "weight": 6,
        "age": 1,
        "egg_quantity": 15
    }
]
```
# List of all chickens with detailed information about their breeds and cages

**URL** : `/chickens/list/nested/`

**Method** : `GET`

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "id": 1,
        "breed": {
            "id": 1,
            "breed": "Broiler",
            "productivity": "high",
            "avg_weight": 5,
            "diet": "Vegetables and crops"
        },
        "cell": {
            "id": 1,
            "cell": 10,
            "row": 10,
            "tsekh": 1
        },
        "weight": 6,
        "age": 1,
        "egg_quantity": 15
    }
]
```

```python
class ChickenNestedSerializer(serializers.ModelSerializer):
    breed = BreedSerializer()
    cell = CellSerializer()

    class Meta:
        model = Chicken
        fields = "__all__"
```

# Update/delete chicken on id

**URL** : `/chickens/info/<int:pk>/`

**Methods** : `PUT` & `DELETE`

**Data constraints** : `{}`

**Generics type** : `RetrieveUpdateDestroyAPIView`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```python
class ChickenChangeInfoAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Chicken.objects.all()
    serializer_class = ChickenRelatedSerializer
```

```python
class ChickenRelatedSerializer(serializers.ModelSerializer):
    breed = serializers.StringRelatedField(read_only=True)
    cell = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Chicken
        fields = "__all__"
```

# Add chicken

**URL** : `/chickens/create/`

**Methods** : `PUT`

**Data constraints** : `{}`

**Generics type** : `CreateAPIView`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```python
class ChickenAddAPIView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ChickenSerializer
    queryset = Chicken.objects.all()
```

```python
class ChickenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chicken
        fields = "__all__"
```

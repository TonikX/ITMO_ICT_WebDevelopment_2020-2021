#Create new chicken

Allows a creation of a new chicken

**URL** : `/chickens/create/`

**Methods** : `PUT`

**Data constraints** : `{}`

**Generics type** : `CreateAPIView`

Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```python
class ChickenCreateAPIView(generics.CreateAPIView):
    serializer_class = ChickenSerializer
    queryset = Chicken.objects.all()
```

```python
class ChickenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chicken
        fields = "__all__"
```


#Update/delete chicken

Allows to delete or update an existing chicken

**URL** : `/chickens/info/<int:pk>/`

**Methods** : `PUT` & `DELETE`

**Data constraints** : `{}`

**Generics type** : `RetrieveUpdateDestroyAPIView`

Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```python
class ChickenInfoAPIView(generics.RetrieveUpdateDestroyAPIView):
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


# List of all chickens

Allow to see a whole chickens information

**URL** : `/chickens/list/`

**Method** : `GET`

**Data constraints** : `{}`

Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "id": 1,
        "breed": "BREED_INFO",
        "cell": "1",
        "weight": 1,
        "age": 1,
        "egg_amount": 1
    }
]
```


# List of all chickens (nested)

Allow to see a whole chickens information (extra details: breed, cells ...)

**URL** : `/chickens/list/nested/`

**Method** : `GET`

**Data constraints** : `{}`

Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "id": 1,
        "breed": {
            "id": 1,
            "breed": "BREED_INFO",
            "productivity": "PRODUCTIVITY_INFO",
            "avg_weight": 1,
            "diet": "DIET_INFO"
        },
        "cell": {
            "id": 1,
            "cell": 11,
            "row": 1,
            "tsekh": 1
        },
        "weight": 1,
        "age": 1,
        "egg_amount": 1
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
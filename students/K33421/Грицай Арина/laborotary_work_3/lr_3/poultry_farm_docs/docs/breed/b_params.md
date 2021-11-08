# List onfo of all breeds

**URL** : `/breeds/list/`

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
        "productivity": "high",
        "avg_weight": 6,
        "diet": "Vegetables, crops"
    },
    {
        "id": 2,
        "breed": "Viandot",
        "productivity": "low",
        "avg_weight": 2,
        "diet": "Vegetables, consumptions"
    }
]
```

# Update/delete breed on id

**URL** : `/breeds/info/<int:pk>/`

**Methods** : `PUT` & `DELETE`

**Data constraints** : `{}`

**Generics type** : `RetrieveUpdateDestroyAPIView`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```python
class BreedChangeInfoAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
```

```python
class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = "__all__"
```

# Add breed

**URL** : `/breeds/create/`

**Methods** : `PUT`

**Data constraints** : `{}`

**Generics type** : `CreateAPIView`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```python
class BreedAddAPIView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BreedSerializer
    queryset = Breed.objects.all()
```

```python
class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = "__all__"
```


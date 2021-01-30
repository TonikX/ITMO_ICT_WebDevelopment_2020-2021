# Create new breed

Allows to create a new breed

**URL** : `/breeds/create/`

**Methods** : `PUT`

**Data constraints** : `{}`

**Generics type** : `CreateAPIView`

Success Responses

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


# Update/delete breed

Allow to update or delete breed info

**URL** : `/breeds/info/<int:pk>/`

**Methods** : `PUT` & `DELETE`

**Data constraints** : `{}`

**Generics type** : `RetrieveUpdateDestroyAPIView`

Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```python
class BreedInfoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
```

```python
class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = "__all__"
```

# List of breeds

Allows to see all breed info

**URL** : `/breeds/list/`

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
        "productivity": "PRODUCTIVITY_INFO",
        "avg_weight": 1,
        "diet": "DIET_INFO"
    },
    {
        "id": 2,
        "breed": "BREED_INFO",
        "productivity": "PRODUCTIVITY_INFO",
        "avg_weight": 1,
        "diet": "DIET_INFO"
    }
]
```
# List of all services

**URL** : `/services/list/`

**Method** : `GET`

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "id": 1,
        "username": "joe_brick",
        "cell": "10",
        "status": true
    },
    {
        "id": 2,
        "username": "ally_milis",
        "cell": "12",
        "status": true
    }
]
```

# List of all services with detailed information about employees and cells

**URL** : `/service/list/nested/`

**Method** : `GET`

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "id": 1,
        "username": {
            "first_name": "Joe",
            "last_name": "Brick",
            "username": "joe_brick",
            "passport": "9999 4566547",
            "salary": 10000,
            "cell": [
                1
            ]
        },
        "cell": {
            "id": 1,
            "cell": 10,
            "row": 10,
            "tsekh": 1
        },
        "status": true
    },
    {
        "id": 2,
        "username": {
            "first_name": "Ally",
            "last_name": "Milis",
            "username": "ally_milis",
            "passport": "1111 98765432",
            "salary": 15000,
            "cell": [
                2
            ]
        },
        "cell": {
            "id": 2,
            "cell": 12,
            "row": 12,
            "tsekh": 2
        },
        "status": true
    }
]
```

```python
class ServiceNestedSerializer(serializers.ModelSerializer):
    username = UserSerializer()
    cell = CellSerializer()

    class Meta:
        model = Service
        fields = "__all__"
```

# Update/delete service on id

**URL** : `/services/info/<int:pk>/`

**Methods** : `PUT` & `DELETE`

**Data constraints** : `{}`

**Generics type** : `RetrieveUpdateDestroyAPIView`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```python
class ServiceChangeInfoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
```

```python
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"
```

# Add service

**URL** : `/service/create/`

**Methods** : `PUT`

**Data constraints** : `{}`

**Generics type** : `CreateAPIView`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```python
class ServiceAddAPIView(generics.CreateAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
```

```python
class ServiceRelatedSerializer(serializers.ModelSerializer):
    username = serializers.StringRelatedField(read_only=True)
    cell = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Service
        fields = "__all__"
```

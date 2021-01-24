# Create service

Allows to create services

**URL** : `/service/create/`

**Methods** : `PUT`

**Data constraints** : `{}`

**Generics type** : `CreateAPIView`

Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```python
class ServiceCreateAPIView(generics.CreateAPIView):
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


# Update/delete service

Allows to update or delete service information

**URL** : `/services/info/<int:pk>/`

**Methods** : `PUT` & `DELETE`

**Data constraints** : `{}`

**Generics type** : `RetrieveUpdateDestroyAPIView`

Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```python
class ServiceInfoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
```

```python
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"
```


# List of services

Allows to see whole information about services

**URL** : `/services/list/`

**Method** : `GET`

**Data constraints** : `{}`

Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "id": 1,
        "username": "DanteLeapman",
        "cell": "1",
        "status": true
    },
    {
        "id": 2,
        "username": "test123",
        "cell": "2",
        "status": true
    }
]
```

# List of services (nested)

Allows to see whole information about services (includes additional info about users)

**URL** : `/service/list/nested/`

**Method** : `GET`

**Data constraints** : `{}`

Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "id": 1,
        "username": {
            "first_name": "Dante",
            "last_name": "Leapman",
            "username": "DanteLeapman",
            "passport": "6666 666666",
            "salary": 666666,
            "cell": [
                2
            ]
        },
        "cell": {
            "id": 1,
            "cell": 1,
            "row": 1,
            "tsekh": 1
        },
        "status": true
    },
    {
        "id": 2,
        "username": {
            "first_name": "Test",
            "last_name": "Test",
            "username": "test123",
            "passport": "1111 111111",
            "salary": 100000,
            "cell": [
                2
            ]
        },
        "cell": {
            "id": 2,
            "cell": 2,
            "row": 1,
            "tsekh": 1
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
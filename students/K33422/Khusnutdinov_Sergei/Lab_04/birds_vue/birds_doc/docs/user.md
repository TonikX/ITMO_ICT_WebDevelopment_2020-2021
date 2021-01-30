# Update/delete user

Allows to update or delete user information

**URL** : `/users/info/<int:pk>/`

**Methods** : `PUT` & `DELETE`

**Data constraints** : `{}`

**Generics type** : `RetrieveUpdateDestroyAPIView`

Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```python
class UserInfoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
```

```python
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
```


# List of users

Allows to see whole user information

**URL** : `/users/list/`

**Method** : `GET`

**Data constraints** : `{}`

Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "first_name": "Test",
        "last_name": "Test",
        "username": "test123",
        "passport": "1111 111111",
        "salary": 100000,
        "cell": [
	   2
	]
    },
    {
        "first_name": "Dante",
        "last_name": "Leapman",
        "username": "DanteLeapman",
        "passport": "6666 666666",
        "salary": 666666,
        "cell": [
            1
        ]
    }
]
```
# List of all users

Выводит информацию обо всех пользователях

**URL** : `/users/list/`

**Method** : `GET`

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "first_name": "Joe",
        "last_name": "Brick",
        "username": "joe_brick",
        "passport": "9999 4566547",
        "salary": 10000,
        "cell": [
            10
        ]
    },
    {
        "first_name": "Ally",
        "last_name": "Milis",
        "username": "ally_milis",
        "passport": "1111 98765432",
        "salary": 15000,
        "cell": [
            12
        ]
    }
]
```

# Update/delete user on id

**URL** : `/users/info/<int:pk>/`

**Methods** : `PUT` & `DELETE`

**Data constraints** : `{}`

**Generics type** : `RetrieveUpdateDestroyAPIView`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```python
class UserChangeInfoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
```

```python
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
```
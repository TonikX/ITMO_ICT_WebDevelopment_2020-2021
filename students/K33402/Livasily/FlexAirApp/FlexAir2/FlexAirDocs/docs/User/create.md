# Create user

Создает нового юзера

**URL** : `/User/create/`

**Methods** : `PUT`

**Data constraints** : `{}`

**Generics type** : `CreateAPIView`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```python
class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
```

```python
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = fields = ['first_name', 'last_name', 'username', 'passport']
```


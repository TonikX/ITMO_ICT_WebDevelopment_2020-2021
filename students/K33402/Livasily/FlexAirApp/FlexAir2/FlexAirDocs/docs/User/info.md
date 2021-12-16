# info user

показывает информацию о новом юзере

**URL** : `/User/info/`

**Methods** : `PUT`

**Data constraints** : `{}`

**Generics type** : `CreateAPIView`

## Success Responses

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
        fields = fields = ['first_name', 'last_name', 'username', 'passport']
```

# Create Author

Создает страницу автора

**URL** : `authors/create/`

**Methods** : `POST`

**Data constraints** : `{}`

**Generics type** : `CreateAPIView`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```python
class AuthorCreateAPIView(CreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
```

```python
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"
```
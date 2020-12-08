# Update Author

Обновляет информацию об определенном авторе

**URL** : `authors/<int:pk>/update/`

**Methods** : `POST`

**Data constraints** : `{}`

**Generics type** : `UpdateAPIView`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```python
class AuthorUpdateAPIView(UpdateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    lookup_field = 'pk'
```

```python
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"
```
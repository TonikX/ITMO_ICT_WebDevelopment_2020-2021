# Delete Author

Удаляет информацию об определенном авторе

**URL** : `authors/<int:pk>/delete/`

**Methods** : `POST`

**Data constraints** : `{}`

**Generics type** : `DeleteAPIView`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```python
class AuthorUpdateAPIView(DeleteAPIView):
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
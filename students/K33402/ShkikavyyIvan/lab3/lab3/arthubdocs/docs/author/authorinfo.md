# Info about Author

Выводит информацию об определенном авторе

**URL** : `authors/<int:pk>/`

**Methods** : `GET`

**Data constraints** : `{}`

**Generics type** : `RetrieveAPIView`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```python
class AuthorRetrieveAPIView(RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
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
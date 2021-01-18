# Delete Author

Удаляет информацию об определенном авторе

**URL** : `authors/<int:pk>/delete/`

**Methods** : `DELETE`

**Data constraints** : `{}`

**Generics type** : `DestroyAPIView`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```python
class AuthorDeleteAPIView(DestroyAPIView):
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
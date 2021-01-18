# Info about Author

Выводит информацию об авторе

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
```

```python
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"
```

```json
{
    "id": 1,
    "name": "Александр Сергеевич Пушкин",
    "description": "русский поэт, драматург и прозаик, заложивший основы русского реалистического направления, критик и теоретик литературы, историк, публицист; один из самых авторитетных литературных деятелей первой трети XIX века.  Ещё при жизни Пушкина сложилась его репутация величайшего национального русского поэта. Пушкин рассматривается как основоположник современного русского литературного языка."
}
```
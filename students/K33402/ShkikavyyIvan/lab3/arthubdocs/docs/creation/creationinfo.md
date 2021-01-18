# Info about Creation

Выводит информацию об определенном произведении автора

**URL** : `creations/<int:pk>/`

**Methods** : `GET`

**Data constraints** : `{}`

**Generics type** : `RetrieveAPIView`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```python
class CreationRetrieveAPIView(RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CreationFullSerializer
    queryset = Creation.objects.all()
```

```python
class CreationFullSerializer(serializers.ModelSerializer):
    creator = AuthorSerializer()

    class Meta:
        model = Creation
        fields = "__all__"
```

```json
{
  "id": 1,
  "creator": {
    "id": 1,
    "name": "Александр Сергеевич Пушкин",
    "description": "русский поэт, драматург и прозаик, заложивший основы русского реалистического направления, критик и теоретик литературы, историк, публицист; один из самых авторитетных литературных деятелей первой трети XIX века.  Ещё при жизни Пушкина сложилась его репутация величайшего национального русского поэта. Пушкин рассматривается как основоположник современного русского литературного языка."
  },
  "name": "Капитанская дочка",
  "description": "исторический роман Александра Пушкина, действие которого происходит во время восстания Емельяна Пугачёва. Впервые опубликован без указания имени автора в 4-й книжке журнала «Современник», поступившей в продажу в последней декаде 1836 года.",
  "type": "Литература"
}
```
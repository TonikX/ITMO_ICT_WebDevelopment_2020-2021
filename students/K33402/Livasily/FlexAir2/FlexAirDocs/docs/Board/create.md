# Create Board

Создает новый борт

**URL** : `/Board/create/`

**Methods** : `PUT`

**Data constraints** : `{}`

**Generics type** : `CreateAPIView`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```python
class BoardListAPIView(generics.ListAPIView):
    serializer_class = BoardSerializer
    queryset = Board.objects.all()
```

```python
class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = "__all__"
```


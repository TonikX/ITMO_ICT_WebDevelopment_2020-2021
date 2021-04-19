# Create Comments

Создает новый отзыв на перелет

**URL** : `/comments`

**Methods** : `PUT`

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

## Code

```python
class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = CommentsSerializer
```

```python
class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
```


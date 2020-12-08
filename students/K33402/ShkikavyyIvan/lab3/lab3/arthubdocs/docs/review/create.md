# Create Review

Создает отзыв

**URL** : `reviews/create/`

**Methods** : `POST`

**Data constraints** : `{}`

**Generics type** : `CreateAPIView`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```python
class CreationCreateAPIView(CreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = CreationSerializer
    queryset = Creation.objects.all()
```

```python
class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Review
        fields = "__all__"
```
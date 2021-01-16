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
class ReviewCreateAPIView(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
```

```python
class ReviewSerializer(serializers.ModelSerializer):
    author = UserNameSerializer(default=serializers.CurrentUserDefault())

    class Meta:
        model = Review
        fields = "__all__"
```
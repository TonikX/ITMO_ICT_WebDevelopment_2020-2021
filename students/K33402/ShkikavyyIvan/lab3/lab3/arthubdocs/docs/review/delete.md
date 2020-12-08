# Delete Review

Удаляет информацию об определенном авторе

**URL** : `reviews/<int:pk>/delete/`

**Methods** : `POST`

**Data constraints** : `{}`

**Generics type** : `DeleteAPIView`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```python
class ReviewDeleteAPIView(DestroyAPIView):
    permission_classes = [IsReviewer]
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    lookup_field = 'pk'
```

```python
class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Review
        fields = "__all__"
```
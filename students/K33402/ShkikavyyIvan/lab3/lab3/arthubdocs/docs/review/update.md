# Update Review

Обновляет информацию об определенном review

**URL** : `reviews/<int:pk>/update/`

**Methods** : `POST`

**Data constraints** : `{}`

**Generics type** : `UpdateAPIView`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```python
class ReviewUpdateAPIView(UpdateAPIView):
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
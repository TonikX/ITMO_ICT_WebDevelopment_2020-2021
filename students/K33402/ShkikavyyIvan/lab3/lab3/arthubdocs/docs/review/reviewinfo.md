# Info about Review

Выводит информацию об определенном review

**URL** : `reviews/<int:pk>/`

**Methods** : `GET`

**Data constraints** : `{}`

**Generics type** : `RetrieveAPIView`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```python
class ReviewRetrieveAPIView(RetrieveAPIView):
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
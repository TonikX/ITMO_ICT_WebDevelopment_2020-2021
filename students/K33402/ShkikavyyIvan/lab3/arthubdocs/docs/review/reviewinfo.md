# Reviews of creation

Выводит информацию об отзывах на определенное произведение

**URL** : `reviews/creation/<int:creationId>/`

**Methods** : `GET`

**Data constraints** : `{}`

**Generics type** : `APIView`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```python
class ReviewListCreationAPIView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

    def get_queryset(self):
        return Review.objects.filter(creation=self.kwargs["creationId"])
```

```python
class ReviewFullSerializer(serializers.ModelSerializer):
    author = UserSerializer(default=serializers.CurrentUserDefault())
    creation = CreationSerializer()

    class Meta:
        model = Review
        fields = "__all__"
```
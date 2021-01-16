# Update Review

Обновляет определенный отзыв

**URL** : `reviews/<int:pk>/update/`

**Methods** : `PATCH`

**Data constraints** : `{}`

**Generics type** : `UpdateAPIView`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```python
class IsReviewer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user == Review.objects.get(pk=view.kwargs['pk']).author
    
class ReviewUpdateAPIView(UpdateAPIView):
    permission_classes = [IsReviewer]
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
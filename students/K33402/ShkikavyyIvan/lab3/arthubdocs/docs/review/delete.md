# Delete Review

Удаляет отзыв

**URL** : `reviews/<int:pk>/delete/`

**Methods** : `DELETE`

**Data constraints** : `{}`

**Generics type** : `DestroyAPIView`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```python
class IsReviewer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user == Review.objects.get(pk=view.kwargs['pk']).author
    
class ReviewDeleteAPIView(DestroyAPIView):
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
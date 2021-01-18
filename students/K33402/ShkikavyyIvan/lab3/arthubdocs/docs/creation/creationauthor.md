# Creations of author

Вывод произведения автора

**URL** : `authors/creation/<int:authorId>/`

**Methods** : `GET`

**Data constraints** : `{}`

**Generics type** : `ListAPIView`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```python
class CreationListAuthorAPIView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CreationSerializer
    queryset = Creation.objects.all()

    def get_queryset(self):
        return Creation.objects.filter(creator=self.kwargs["authorId"])
```

```python
class CreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creation
        fields = "__all__"
```
# Delete Creation

Удаляет информацию об определенном произведении

**URL** : `creations/<int:pk>/delete/`

**Methods** : `POST`

**Data constraints** : `{}`

**Generics type** : `DeleteAPIView`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```python
class CreationDeleteAPIView(DestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = CreationSerializer
    queryset = Creation.objects.all()
    lookup_field = 'pk'
```

```python
class CreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creation
        fields = "__all__"
```
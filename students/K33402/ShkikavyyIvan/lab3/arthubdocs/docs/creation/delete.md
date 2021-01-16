# Delete Creation

Удаляет произведение 

**URL** : `creations/<int:pk>/delete/`

**Methods** : `DELETE`

**Data constraints** : `{}`

**Generics type** : `DestroyAPIView`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```python
class CreationDeleteAPIView(DestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = CreationSerializer
    queryset = Creation.objects.all()
```

```python
class CreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creation
        fields = "__all__"
```
# Update Creator

Обновляет информацию об определенном произведении

**URL** : `creations/<int:pk>/update/`

**Methods** : `POST`

**Data constraints** : `{}`

**Generics type** : `UpdateAPIView`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```python
class CreationUpdateAPIView(UpdateAPIView):
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
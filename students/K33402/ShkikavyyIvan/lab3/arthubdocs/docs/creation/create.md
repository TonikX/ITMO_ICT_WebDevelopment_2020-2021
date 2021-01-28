# Create Creation

Создает страницу произведения

**URL** : `creations/create/`

**Methods** : `POST`

**Data constraints** : `{}`

**Generics type** : `CreateAPIView`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```python
class CreationCreateAPIView(CreateAPIView):
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
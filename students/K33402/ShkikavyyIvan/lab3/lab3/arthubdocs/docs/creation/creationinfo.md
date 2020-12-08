# Info about Creation

Выводит информацию об определенном произведении

**URL** : `creations/<int:pk>/`

**Methods** : `GET`

**Data constraints** : `{}`

**Generics type** : `RetrieveAPIView`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```python
class CreationRetrieveAPIView(RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
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
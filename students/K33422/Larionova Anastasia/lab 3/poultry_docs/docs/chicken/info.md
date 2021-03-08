# Update/delete chicken

Позволяет обновлять или удалять информацию о курице по id

**URL** : `/chickens/info/<int:pk>/`

**Methods** : `PUT` & `DELETE`

**Data constraints** : `{}`

**Generics type** : `RetrieveUpdateDestroyAPIView`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```python
class ChickenInfoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chicken.objects.all()
    serializer_class = ChickenRelatedSerializer
```

```python
class ChickenRelatedSerializer(serializers.ModelSerializer):
    breed = serializers.StringRelatedField(read_only=True)
    cell = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Chicken
        fields = "__all__"
```
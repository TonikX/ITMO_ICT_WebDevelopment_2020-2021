## Create Movie
Создаем фильм

**URL** : /movie/create/

**Methods** : PUT

**Data constraints** : {}

**Generics type** : CreateAPIView

Success Responses


## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = HotelSerializer

```
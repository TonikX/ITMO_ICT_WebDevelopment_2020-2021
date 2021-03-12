## Вывод полной информации о всех войнах и их профессиях (в одном запросе)
 _views.py_
```
class Task1(generics.ListAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorProfessionSerializer
```
_serializators.py_
```
class WarriorProfessionSerializer(serializers.ModelSerializer):

    profession = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Warrior
        fields = ["name", "profession"]
```
_urls.py_
```
from django.urls import path
from .views import *

urlpatterns = [
    ...
    path('warriors/list_p/', Task1.as_view()),
    ...
]
```
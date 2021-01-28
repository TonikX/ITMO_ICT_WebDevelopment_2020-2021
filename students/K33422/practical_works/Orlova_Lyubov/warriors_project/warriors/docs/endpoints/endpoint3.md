## Вывод полной информации о войне (по id), его профессиях и скилах.
 _views.py_
```
class Task3(generics.RetrieveUpdateAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorRelatedSerializer
```
_serializators.py_
```
class WarriorRelatedSerializer(serializers.ModelSerializer):
    # skill = serializers.SlugRelatedField(read_only=True, many=True, slug_field='title')
    skill = serializers.StringRelatedField(read_only=True, many=True)
    profession = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Warrior
        fields = ["name", "profession", "skill"]
```
_urls.py_
```
from django.urls import path
from .views import *

urlpatterns = [
    ...
    path('warriors/<int:pk>/info/', Task3.as_view()),
    ...
]
```
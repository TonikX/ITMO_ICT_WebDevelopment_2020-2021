# Практическое задание №3.2: Документирование.
---
## Задание1: Реализовать ендпоинты для добавления и просмотра скилов
### Добавление:
 views.py
```
class SkillCreateView(APIView):

   def post(self, request):

        skill = request.data.get("skill")
        serializer = SkillCreateSerializer(data=skill)

        if serializer.is_valid(raise_exception=True):
            skill_saved = serializer.save()

        return Response({"Success": "Skill '{}' created succesfully.".format(skill_saved.title)})
```
serializators.py
```
class SkillCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)

    def create(self, validated_data):
        skill = Skill(**validated_data)
        skill.save()
        return Skill(**validated_data)
```

### Просмотр:
 views.py
```
class SkillAPIView(APIView):

   def get(self, request):

        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response({"Skills": serializer.data})
```
serializators.py
```
class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = "__all__"
```
### Url-файл
urls.py
```
from django.urls import path
from .views import *

urlpatterns = [
    ...
    path('skill/', SkillAPIView.as_view()),
    path('skill/create/', SkillCreateView.as_view()),
    ...
]
```
---
## Задание2:
## 1. Вывод полной информации о всех войнах и их профессиях (в одном запросе).
 views.py
```
class Task1(generics.ListAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorProfessionSerializer
```
serializators.py
```
class WarriorProfessionSerializer(serializers.ModelSerializer):

    profession = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Warrior
        fields = ["name", "profession"]
```
urls.py
```
from django.urls import path
from .views import *

urlpatterns = [
    ...
    path('warriors/list_p/', Task1.as_view()),
    ...
]
```
## 2. Вывод полной информации о всех войнах и их скилах (в одном запросе).
 views.py
```
class Task2(generics.ListAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSkillSerializer
```
serializators.py
```
class WarriorSkillSerializer(serializers.ModelSerializer):

    skill = serializers.StringRelatedField(read_only=True, many=True)

    class Meta:
        model = Warrior
        fields = ["name", "skill"]
```
urls.py
```
from django.urls import path
from .views import *

urlpatterns = [
    ...
    path('warriors/list_sk/', Task2.as_view()),
    ...
]
```
## 3. Вывод полной информации о войне (по id), его профессиях и скилах.
 views.py
```
class Task3(generics.RetrieveUpdateAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorRelatedSerializer
```
serializators.py
```
class WarriorRelatedSerializer(serializers.ModelSerializer):
    # skill = serializers.SlugRelatedField(read_only=True, many=True, slug_field='title')
    skill = serializers.StringRelatedField(read_only=True, many=True)
    profession = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Warrior
        fields = ["name", "profession", "skill"]
```
urls.py
```
from django.urls import path
from .views import *

urlpatterns = [
    ...
    path('warriors/<int:pk>/info/', Task3.as_view()),
    ...
]
```
## 4. Удаление война по id.
 views.py
```
class Task4(generics.RetrieveDestroyAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorRelatedSerializer
```
serializators.py
```
class WarriorRelatedSerializer(serializers.ModelSerializer):
    # skill = serializers.SlugRelatedField(read_only=True, many=True, slug_field='title')
    skill = serializers.StringRelatedField(read_only=True, many=True)
    profession = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Warrior
        fields = ["name", "profession", "skill"]
```
urls.py
```
from django.urls import path
from .views import *

urlpatterns = [
    ...
    path('warriors/<int:pk>/delete/', Task4.as_view()),
    ...
]
```
## 5. Редактирование информации о войне.
 views.py
```
class Task5(generics.RetrieveUpdateAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer
```
serializators.py
```
class WarriorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Warrior
        fields = "__all__"
```
urls.py
```
from django.urls import path
from .views import *

urlpatterns = [
    ...
    path('warriors/<int:pk>/update/', Task5.as_view()),
]
```




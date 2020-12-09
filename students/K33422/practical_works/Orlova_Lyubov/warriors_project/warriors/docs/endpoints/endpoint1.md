## Ендпоинты для добавления скилов
 _views.py_
```
class SkillCreateView(APIView):

   def post(self, request):

        skill = request.data.get("skill")
        serializer = SkillCreateSerializer(data=skill)

        if serializer.is_valid(raise_exception=True):
            skill_saved = serializer.save()

        return Response({"Success": "Skill '{}' created succesfully.".format(skill_saved.title)})
```
_serializators.py_
```
class SkillCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)

    def create(self, validated_data):
        skill = Skill(**validated_data)
        skill.save()
        return Skill(**validated_data)
```

_urls.py_
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
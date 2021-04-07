## Просмотр списка скилов методом, описанным в пункте 3
_serializators.py_
```
class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = "__all__"
```
 _views.py_
```
class SkillAPIView(APIView):
    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response({"Skills": serializer.data})
```

_urls.py_
```
...

urlpatterns = [
    ...
    path('skills/', SkillAPIView.as_view()),
    ...
]
```
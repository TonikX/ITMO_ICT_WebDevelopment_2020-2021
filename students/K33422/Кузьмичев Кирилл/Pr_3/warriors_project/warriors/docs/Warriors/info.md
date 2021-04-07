## Вывод полной информации о войне (по id), его профессиях и скилах.

_serializators.py_
```
class WarriorRelatedSerializer(serializers.ModelSerializer):
    skill = serializers.StringRelatedField(read_only=True, many=True)
    profession = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Warrior
        fields = ["name", "profession", "skill"]
```
 _views.py_
```
class WarriorInfoAPIView(generics.RetrieveAPIView):
    serializer_class = WarriorRelatedSerializer
    queryset = Warrior.objects.all()
```

_urls.py_
```
...

urlpatterns = [
    ...
    path('warriors/info/<int:pk>/', WarriorInfoAPIView.as_view()),
    ...
]
```
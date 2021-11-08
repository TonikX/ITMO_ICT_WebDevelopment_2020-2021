## Вывод полной информации о всех войнах и их профессиях (в одном запросе).
_serializators.py_
```
class WarriorProfessionSerializer(serializers.ModelSerializer):
    profession = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Warrior
        fields = ["name", "profession"]
```
 _views.py_
```
class WarriorProfessionListAPIView(generics.ListAPIView):
    serializer_class = WarriorProfessionSerializer
    queryset = Warrior.objects.all()
```

_urls.py_
```
...

urlpatterns = [
    ...
    'warriors/profession_list/', WarriorProfessionListAPIView.as_view()),
    ...
]
```
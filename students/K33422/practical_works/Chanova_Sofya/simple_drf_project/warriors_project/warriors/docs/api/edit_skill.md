# update a warrior's skill

edit skill information of a particular warrior

**URL** : `api/warriors/<int:pk>/edit_skill`

**Method** : `POST`

**Data constraints** : `{}`

**Content-Type** : application/json

**Python code** :
```python
class EditWarriorSkillAPIView(generics.UpdateAPIView):

    serializer_class = SkillOfWarriorSerializer
    queryset = SkillOfWarrior.objects.all()
```
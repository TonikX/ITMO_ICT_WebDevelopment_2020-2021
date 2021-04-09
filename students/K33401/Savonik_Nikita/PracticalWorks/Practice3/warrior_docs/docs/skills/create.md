**URL** : `/skill/create/`

**HTTP 200 OK**

**Allow** : POST, OPTIONS

**Content-Type** : application/json

**Vary** : Accept
```python
# serializer.py
class SkillCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)

    def create(self, validated_data):
        skill = Skill(**validated_data)
        skill.save()
        return Skill(**validated_data)

# views.py
class SkillCreateView(APIView):
    def post(self, request):
        skills = request.data.get("skill")
        serializer = SkillCreateSerializer(data=skills)

        if serializer.is_valid(raise_exception=True):
            skill_saved = serializer.save()
            return Response({"Success": "Skill '{}' created succesfully.".format(skill_saved.title)})
```
from rest_framework import serializers
from .models import *
from rest_framework import generics


class WarriorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warrior
        fields = "__all__"


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ["title"]


class SkillCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)

    def create(self, validated_data):
        skill = Skill(**validated_data)
        skill.save()
        return Skill(**validated_data)


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ["title"]


class SkillOfWarriorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillOfWarrior
        fields = ["skill", "level"]


class ProfessionRelatedSerializer(serializers.ModelSerializer):
    profession = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Warrior
        fields = ["name", "profession"]


class SkillRelatedSerializer(serializers.ModelSerializer):
    skill = serializers.StringRelatedField(read_only=True, many=True)
    name = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = SkillOfWarrior
        fields = ["name", "skill"]


class WarriorGetView(generics.DestroyAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer


class WarriorDestroyView(generics.DestroyAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer


class WarriorUpdateView(generics.UpdateAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer


class SkillOfWarriorUpdateView(generics.UpdateAPIView):
    queryset = SkillOfWarrior.objects.all()
    serializer_class = SkillOfWarriorSerializer
from rest_framework import serializers
from .models import *


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = "__all__"


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['title']


class SkillOfWarriorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillOfWarrior
        fields = "__all__"


class WarriorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warrior
        fields = "__all__"


class SkillCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)

    def create(self, validated_data):
        skill = Skill(**validated_data)
        skill.save()
        return Skill(**validated_data)


class WarriorProfessionNestedSerializer(serializers.ModelSerializer):
    profession = ProfessionSerializer()

    class Meta:
        model = Warrior
        fields = "__all__"


class WarriorSkillNestedSerializer(serializers.ModelSerializer):
    skill = SkillSerializer(many=True)

    class Meta:
        model = Warrior
        fields = "__all__"

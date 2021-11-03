from rest_framework import serializers
from .models import *


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = "__all__"


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"


class SkillOfWarriorSerializer(serializers.ModelSerializer):

    skill = SkillSerializer()

    class Meta:
        model = SkillOfWarrior
        fields = ['skill', 'level']


class WarriorSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, required=False)

    class Meta:
        model = Warrior
        fields = "__all__"


class ProfessionCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    description = serializers.CharField()

    def create(self, validated_data):
        profession = Profession(**validated_data)
        profession.save()
        return Profession(**validated_data)


class SkillRelatedSerializer(serializers.ModelSerializer):
    warrior_skills = WarriorSerializer(many=True)

    class Meta:
        model = Skill
        fields = ["title", "warrior_skills"]


class WarriorSkillsSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True)

    class Meta:
        model = Warrior
        fields = "__all__"


class WarriorProfSerializer(serializers.ModelSerializer):

    profession = ProfessionSerializer()

    class Meta:
        model = Warrior
        fields = "__all__"


class OneWarriorSerializer(serializers.ModelSerializer):

    profession = ProfessionSerializer()
    skills = SkillSerializer(many=True)

    class Meta:
        model = Warrior
        fields = "__all__"
        read_only_fields = ['id']

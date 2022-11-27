from rest_framework import serializers
from .models import *


class WarriorBaseSerializer(serializers.ModelSerializer):
    race = serializers.CharField(source="get_race_display")

    class Meta:
        model = Warrior
        fields = ["id", "name", "race", "level"]


class WarriorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warrior
        fields = "__all__"


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = "__all__"


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"


class SkillOfWarriorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillOfWarrior
        fields = "__all__"


class WarriorWithProfSerializer(serializers.ModelSerializer):
    race = serializers.CharField(source="get_race_display")
    profession = ProfessionSerializer()

    class Meta:
        model = Warrior
        fields = ["id", "name", "race", "level", "profession"]


class WarriorWithSkillsSerializer(serializers.ModelSerializer):
    race = serializers.CharField(source="get_race_display")
    skill = serializers.StringRelatedField(read_only=True, many=True)

    class Meta:
        model = Warrior
        fields = ["id", "name", "race", "level", "skill"]


class WarriorDetailSerializer(serializers.ModelSerializer):
    race = serializers.CharField(source="get_race_display")

    class Meta:
        model = Warrior
        fields = "__all__"
        depth = 1

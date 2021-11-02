from rest_framework import serializers
from .models import *


class SkillSerializer(serializers.ModelSerializer):

	class Meta:
		model = Skill
		fields = "__all__"


class WarriorSerializer(serializers.ModelSerializer):

	class Meta:
		model = Warrior
		fields = "__all__"


class ProfessionSerializer(serializers.ModelSerializer):

	class Meta:
		model = Profession
		fields = "__all__"


class WarriorNestedSerializer(serializers.ModelSerializer):
    # делаем наследование
    profession = ProfessionSerializer()
    # skill = SkillSerializer(many=True)

    # уточняем поле
    # race = serializers.CharField(source="get_race_display", read_only=True)

    class Meta:
    	model = Warrior
    	fields = "__all__"


class WarriorSkillsSerializer(serializers.ModelSerializer):
    # делаем наследование
    # profession = ProfessionSerializer()
    skill = SkillSerializer(many=True)

    # уточняем поле
    # race = serializers.CharField(source="get_race_display", read_only=True)

    class Meta:
    	model = Warrior
    	fields = "__all__"


class WarriorFullSerializer(serializers.ModelSerializer):
    # делаем наследование
    profession = ProfessionSerializer(read_only=True)
    skill = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = Warrior
        fields = "__all__"
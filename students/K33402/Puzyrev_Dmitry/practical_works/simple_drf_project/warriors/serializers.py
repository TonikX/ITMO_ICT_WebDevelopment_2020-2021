from rest_framework import serializers
from .models import *

class WarriorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Warrior
    fields = ['name']


class WarriorRelatedSerializer(serializers.ModelSerializer):
  skill = serializers.StringRelatedField(read_only=True, many=True)
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


class SkillRelatedSerializer(serializers.ModelSerializer):
  warrior_skills = WarriorSerializer(many=True)

  class Meta:
    model = Skill
    fields = ['title', 'warrior_skills']
  

class WarriorNestedSerializer(serializers.ModelSerializer):
  profession = ProfessionSerializer()
  skill = SkillSerializer(many=True)
  race = serializers.CharField(source="get_race_display", read_only=True)
  class Meta:
    model = Warrior
    fields = "__all__"
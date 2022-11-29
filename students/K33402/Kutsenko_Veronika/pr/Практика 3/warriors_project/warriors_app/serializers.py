from rest_framework import serializers
from .models import *

class ProfessionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profession
        fields = ["title", "description"]
        
        
class SkillSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Skill
        fields = ["title"]
        
 
class WarriorAndProfessionSerializer(serializers.ModelSerializer):
    profession = ProfessionSerializer()

    class Meta:
        model = Warrior
        fields = ["id", "name", "race", "level", "profession"]


class WarriorAndSkillSerializer(serializers.ModelSerializer):
    skill = serializers.SlugRelatedField(read_only=True, many=True, slug_field='title')

    class Meta:
        model = Warrior
        fields = ["id", "name", "race", "level", "skill"]
        
        
class WarriorSerializer(serializers.ModelSerializer):
    profession = ProfessionSerializer()
    skill = SkillSerializer(many=True)
    
    class Meta:
        model = Warrior
        fields = ["id", "name", "race", "level", "profession", "skill"]
        
        
class WarriorUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Warrior
        fields = "__all__"
        
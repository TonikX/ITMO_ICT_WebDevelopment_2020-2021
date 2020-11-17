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
        fields = fields = ["id", "name", "race", "level", "skill"]
        
        
class WarriorSerializer(serializers.ModelSerializer):
     
    def update(self, instance, validated_data):
        instance.race = validated_data.get('race', instance.race)
        instance.name = validated_data.get('name', instance.name)
        instance.skill = validated_data.get('skill', instance.skill)
        instance.profession = validated_data.get('profession', instance.author_id)
        instance.save()
        return instance
        
    class Meta:
        model = Warrior
        fields = fields = ["id", "name", "race", "level", "profession", "skill"]
        depth = 1
        
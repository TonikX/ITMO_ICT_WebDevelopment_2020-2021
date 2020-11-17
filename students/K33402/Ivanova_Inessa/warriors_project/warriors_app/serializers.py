from rest_framework import serializers
from .models import *

class WarriorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Warrior
        fields = "__all__"
        
        
class ProfessionCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    description = serializers.CharField()
    
    def create(self, validated_data):
        return Profession(**validated_data)
        
        
class ProfessionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profession
        fields = ["title", "description"]
        
        
class SkillSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Skill
        fields = "__all__"
        
        
class SkillCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    
    def create(self, validated_data):
        return Skill(**validated_data)
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
        profession = Profession(**validated_data)
        profession.save()
        return Profession(**validated_data)


class SkillCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)

    def create(self, validated_data):
        skill = Skill(**validated_data)
        skill.save()
        return Skill(**validated_data)


class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = "__all__"


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = "__all__"


class WarriorCreateSerializer(serializers.Serializer):
    profession = ProfessionSerializer()
    skill = SkillSerializer(many=True)
    race = serializers.CharField(source="get_race_display", read_only=True)

    class Meta:
        model = Warrior
        fields = "__all__"

    def create(self, validated_data):
        profession = Profession.objects.create(title=validated_data['profession']['title'],
                                               description=validated_data['profession']['description'])
        profession.save()
        instance = Warrior.objects.create(name=validated_data['name'], level=validated_data['level'],
                                          profession=profession)
        for skill in validated_data['skill']:
            skill_obj = Skill.objects.create(**skill)
            skill_obj.save()
            skill_of_warrior = SkillOfWarrior.objects.create(skill=skill_obj, warrior=instance)
            skill_of_warrior.save()

        return instance


class WarriorProfessionSerializer(serializers.ModelSerializer):
    profession = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Warrior
        fields = ["name", "profession"]


class WarriorSkillSerializer(serializers.ModelSerializer):
    skill = serializers.StringRelatedField(read_only=True, many=True)

    class Meta:
        model = Warrior
        fields = ["name", "skill"]


class WarriorRelatedSerializer(serializers.ModelSerializer):
    skill = serializers.StringRelatedField(read_only=True, many=True)
    profession = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Warrior
        fields = ["name", "profession", "skill"]

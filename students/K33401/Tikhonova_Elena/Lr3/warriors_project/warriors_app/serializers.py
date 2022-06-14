from rest_framework import serializers
from .models import *


class WarriorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Warrior
        fields = "__all__"


# class SkillSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Skill
#         fields = "__all__"


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = "__all__"


class ProfessionCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    description = serializers.CharField()

    def create(self, validated_data):
        profession = Profession(**validated_data)
        profession.save()
        return Profession(**validated_data)


class SkillSerializer(serializers.ModelSerializer):
    warriors = WarriorSerializer(many=True)

    class Meta:
        model = Skill
        fields = ["title", "warriors"]


# class SkillCreateSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=120)

#     def create(self, validated_data):
#         skill = Skill(**validated_data)
#         skill.save()
#         return Skill(**validated_data)


# last part of practice 3.1


class WarriorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warrior
        fields = ['name', 'race', 'level', 'profession']


class SkillCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"


class SkillOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['title']


class SkillOfWarriorSerializer(serializers.ModelSerializer):
    # https://stackoverflow.com/questions/17256724/include-intermediary-through-model-in-responses-in-django-rest-framework

    skill = SkillOnlySerializer()

    class Meta:
        model = SkillOfWarrior
        fields = ['skill', 'level']


# просмотр полной информации о воине


class WarriorRetrieveSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True)
    profession = ProfessionSerializer()
    # возможно, перебор со вложенностью - для каждого скилла показывает еще и инфу о воинах, им обладающих
    # легко исправить, если прописать другой SkillSerializer - без warriors

    class Meta:
        model = Warrior
        fields = ['name', 'race', 'profession', 'level', 'skills']


# вывод полной информации обо всех воинах и скиллах


class WarriorSkillSerializer(serializers.ModelSerializer):

    skillofwarrior_set = SkillOfWarriorSerializer(many=True)

    class Meta:
        model = Warrior
        fields = ['name', 'race', 'profession', 'level', 'skillofwarrior_set']

# инфа о воинах и их профессиях


class WarriorProfessionSerializer(serializers.ModelSerializer):

    profession = ProfessionSerializer()
    skills = SkillOnlySerializer(many=True)

    class Meta:
        model = Warrior
        fields = ['name', 'race', 'profession', 'level', 'skills']

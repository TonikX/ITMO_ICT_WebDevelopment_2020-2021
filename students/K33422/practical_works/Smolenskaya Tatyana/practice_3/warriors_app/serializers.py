from rest_framework import serializers
from .models import Warrior, Profession, Skill, SkillOfWarrior


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
        fields = "__all__"


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"


class SkillOfWarriorSerializer(serializers.ModelSerializer):
    warrior_skills = WarriorSerializer(many=True)

    class Meta:
        model = Skill
        fields = "__all__"


class WarriorRelatedSerializer(serializers.ModelSerializer):
    skill = serializers.StringRelatedField(read_only=True, many=True)

    class Meta:
        model = Warrior
        fields = "__all__"


class WarriorDepthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warrior
        fields = "__all__"

        depth = 1


class WarriorNestedSerializer(serializers.ModelSerializer):
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

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.level = validated_data['level']
        instance.profession.title = validated_data['profession']['title']
        instance.profession.description = validated_data['profession']['description']
        instance.save()
        skills = list(instance.skill.all())

        for input_skill in validated_data['skill']:
            skill = skills.pop(0)
            skill.title = input_skill['title']
            skill.save()

        return instance

    def to_representation(self, instance):
        representation = super(WarriorNestedSerializer, self).to_representation(instance)
        representation['skill'] = SkillOfWarriorSerializer(instance.skill.all(), many=True).data
        return representation

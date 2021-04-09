from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from warriors.models import *
from warriors.serializers import *


class SkillAPIView(APIView):
    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response({"Skills": serializer.data})


class SkillCreateView(APIView):
    def post(self, request):
        skills = request.data.get("skill")
        serializer = SkillCreateSerializer(data=skills)

        if serializer.is_valid(raise_exception=True):
            skill_saved = serializer.save()
            return Response({"Success": "Skill '{}' created succesfully.".format(skill_saved.title)})


class WarriorListAPIView(generics.ListAPIView):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()


class ProfessionCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ProfessionSerializer
    queryset = Profession.objects.all()


class WarriorCreateAPIView(generics.CreateAPIView):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()


class SkillOfWarriorCreateAPIView(generics.CreateAPIView):
    serializer_class = SkillOfWarriorSerializer
    queryset = SkillOfWarrior.objects.all()


class WarriorAllView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()


class WarriorsProfessionSkillView(generics.ListAPIView):
    serializer_class = WarriorProfessionNestedSerializer
    queryset = Warrior.objects.all()


class WarriorsSkillView(generics.ListAPIView):
    serializer_class = WarriorSkillNestedSerializer
    queryset = Warrior.objects.all()

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *


class WarriorAPIView(APIView):
    def get(self, request):
        warriors = Warrior.objects.all()
        serializer = WarriorBaseSerializer(warriors, many=True)
        return Response({"Warriors": serializer.data})


class WarriorWithProfAPIView(APIView):
    def get(self, request):
        warriors = Warrior.objects.all()
        serializer = WarriorWithProfSerializer(warriors, many=True)
        return Response({"Warriors": serializer.data})


class WarriorWithSkillsAPIView(APIView):
    def get(self, request):
        warriors = Warrior.objects.all()
        serializer = WarriorWithSkillsSerializer(warriors, many=True)
        return Response({"Warriors": serializer.data})


class WarriorCreateAPIView(generics.CreateAPIView):
    serializer_class = WarriorBaseSerializer
    queryset = Warrior.objects.all()


class WarriorActionAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WarriorDetailSerializer
    queryset = Warrior.objects.all()


class ProfessionAPIView(APIView):
    def get(self, request):
        professions = Profession.objects.all()
        serializer = ProfessionSerializer(professions, many=True)
        return Response({"Professions": serializer.data})


class ProfessionCreateAPIView(generics.CreateAPIView):
    serializer_class = ProfessionSerializer
    queryset = Profession.objects.all()


class SkillAPIView(APIView):
    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response({"Skills": serializer.data})


class SkillCreateAPIView(generics.CreateAPIView):
    serializer_class = SkillSerializer
    queryset = Skill.objects.all()


class SkillOfWarriorAPIView(APIView):
    def get(self, request):
        skills = SkillOfWarrior.objects.all()
        serializer = SkillOfWarriorSerializer(skills, many=True)
        return Response({"Skills & Warriors": serializer.data})


class SkillOfWarriorCreateAPIView(generics.CreateAPIView):
    serializer_class = SkillOfWarriorSerializer
    queryset = Skill.objects.all()

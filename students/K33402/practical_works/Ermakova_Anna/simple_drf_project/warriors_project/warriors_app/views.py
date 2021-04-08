from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics


class SkillAPIView(APIView):

    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response({"Skills": serializer.data})


class SkillCreateView(APIView):

    def post(self, request):
        skill = request.data.get("skill")
        serializer = SkillSerializer(data=skill)

        if serializer.is_valid(raise_exception=True):
            skill_saved = serializer.save()

        return Response({"Success": "Skill '{}' created".format(skill_saved.title)})


class WarriorAndProfessionAPIView(generics.ListAPIView):
    serializer_class = WarriorAndProfessionSerializer
    queryset = Warrior.objects.all()


class WarriorAndSkillAPIView(generics.ListAPIView):
    serializer_class = WarriorAndSkillSerializer
    queryset = Warrior.objects.all()


class WarriorAPIView(generics.RetrieveAPIView):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()


class WarriorAPIDelete(generics.RetrieveDestroyAPIView):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()


class WarriorAPIUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = WarriorUpdateSerializer
    queryset = Warrior.objects.all()



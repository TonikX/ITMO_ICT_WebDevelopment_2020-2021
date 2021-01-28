from django.shortcuts import render
from rest_framework import serializers, generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from warriors_app.models import Warrior, Skill, Profession
from warriors_app.serializers import WarriorSerializer, SkillSerializer, ProfessionCreateSerializer, \
    WarriorNestedSerializer


class WarriorAPIView(APIView):

    def get(self, request):
        warriors = Warrior.objects.all()
        serializer = WarriorSerializer(warriors, many=True)
        return Response({"Warriors": serializer.data})


class ProfessionCreateView(APIView):
    def post(self, request):
        profession = request.data.get("profession")

        serializer = ProfessionCreateSerializer(data=profession)

        if serializer.is_valid(raise_exception=True):
            profession_saved = serializer.save()

        return Response({"Success": "Profession '{}' created succesfully.".format(profession_saved.title)})


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

        return Response({"Success": "Skill '{}' created succesfully.".format(skill_saved.title)})


class WarriorAndProfessionAPIView(generics.ListAPIView):
    serializer_class = WarriorNestedSerializer
    queryset = Warrior.objects.all()


class WarriorAndSkillAPIView(generics.ListAPIView):
    serializer_class = WarriorNestedSerializer
    queryset = Warrior.objects.all()


class WarriorViewSet(viewsets.ModelViewSet):
    queryset = Warrior.objects.all()
    serializer_class = WarriorNestedSerializer

from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

class WarriorsAndProfessionsAPIView(generics.ListAPIView):
    serializer_class = WarriorNestedSerializer
    queryset = Warrior.objects.all()

class WarriorsAndSkillsAPIView(generics.ListAPIView):
    serializer_class = WarriorSkillsSerializer
    queryset = Warrior.objects.all()

class WarriorGetAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WarriorFullSerializer
    queryset = Warrior.objects.all()

class ProfessionCreateView(APIView):

   def post(self, request):
       profession = request.data.get("profession")
       serializer = ProfessionSerializer(data=profession)

       if serializer.is_valid(raise_exception=True):
           profession_saved = serializer.save()

       return Response({"Success": "Profession '{}' created succesfully.".format(profession_saved.title)})


class SkillCreateView(APIView):

   def post(self, request):
       skill = request.data.get("skill")
       serializer = SkillSerializer(data=skill)

       if serializer.is_valid(raise_exception=True):
           skill_saved = serializer.save()

       return Response({"Success": "Skill '{}' created succesfully.".format(skill_saved.title)})
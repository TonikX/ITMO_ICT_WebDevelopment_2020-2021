from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import generics



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



class SkillCreateAPIView(APIView):
    def post(self, request):
        skill = request.data.get("skill")
        serializer = SkillSerializer(data=skill)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response({"Success": "Created succesfully."})

class SkillGetAPIView(APIView):
    def get(self, request):
        skill = Skill.objects.all()
        serializer = SkillSerializer(skill, many=True)
        return Response({"Skill": serializer.data})


class WarriorsProfession(APIView):
    def get(self, request):
        prof = Warrior.objects.all()
        serializer = WarriorProfSerializer(prof, many=True)
        return Response({"Professions": serializer.data})

class WarriorsSkills(APIView):
    def get(self, request):
        skill = Warrior.objects.all()
        serializer = WarriorSkillsSerializer(skill, many=True)
        return Response({"Skill": serializer.data})


class OneWarriorAPIView(generics.RetrieveAPIView):
    serializer_class = WarriorNestedSerializer
    queryset = Warrior.objects.all()

class OneWarriorEditAPIView(generics.UpdateAPIView):
    serializer_class = WarriorNestedSerializer
    queryset = Warrior.objects.all()
    lookup_field = 'pk'


class OneWarriorDestroyAPIView(generics.DestroyAPIView):
    serializer_class = WarriorNestedSerializer
    queryset = Warrior.objects.all()
    lookup_field = 'pk'
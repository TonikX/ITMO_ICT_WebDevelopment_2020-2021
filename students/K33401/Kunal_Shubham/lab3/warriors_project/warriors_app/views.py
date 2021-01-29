from django.http import Http404
from rest_framework import response, status, mixins, generics
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from .serializers import *
from .models import Warrior

# Create your views here.


class WarriorAPIView(APIView):
    def get(self, request):
        warriors = Warrior.objects.all()
        serializer = WarriorSerializer(warriors, many=True)
        return Response({"Warriors": serializer.data})


class WarriorNestedAPIView(APIView):
    def get_object(self, warrior_id):
        try:
            return Warrior.objects.get(pk=warrior_id)
        except Warrior.DoesNotExist:
            raise Http404

    def get(self, request, warrior_id):
        warrior = self.get_object(warrior_id)
        serializer = WarriorNestedSerializer(warrior)
        return Response({"Warrior": serializer.data})


class WarriorUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer


class WarriorDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer


class ProfessionCreateView(APIView):
    def post(self, request):
        profession = request.data.get("profession")
        serializer = ProfessionCreateSerializer(data=profession)

        if serializer.is_valid(raise_exception=True):
            profession_saved = serializer.save()

        return Response(
            {"Success": f"Profession {profession_saved.title} created succesfully."}
        )


class SkillAPIView(APIView):
    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response({"Skills": serializer.data})

    def post(self, request):
        skill = request.data.get("skill")
        serializer = SkillSerializer(data=skill)

        if serializer.is_valid(raise_exception=True):
            skill_saved = serializer.save()

        return Response({"Success": f"Skill { skill_saved} created succesfully"})

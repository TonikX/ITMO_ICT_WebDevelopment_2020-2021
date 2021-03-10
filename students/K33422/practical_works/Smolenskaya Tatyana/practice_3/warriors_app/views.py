from django.template.defaultfilters import title
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework import generics, status, viewsets

from . import serializers
from .models import Warrior, Skill

from .serializers import WarriorSerializer, WarriorNestedSerializer, SkillSerializer


class WarriorAPIView(APIView):
    def get(self, request):
        warriors = Warrior.objects.all()
        serializer = WarriorSerializer(warriors, many=True)
        return Response({"Warriors": serializer.data})

    def post(self, request):
        serializer = WarriorSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            warrior_saved = serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        warrior = get_object_or_404(Warrior, pk=pk)
        serializer = WarriorSerializer(warrior, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        warrior = get_object_or_404(Warrior, pk=pk)
        try:
            warrior.delete()
            return Response(status=200)
        except:
            return Response(status=400)


class ProfessionCreateView(APIView):
    def post(self, request):
        print("REQUEST DATA: ", request.data)
        profession = request.data.get("profession")
        print("PROF DATA", profession)

        if serializer.is_valid(raise_exception=True):
            profession_saved = serializer.save()

        return Response({"Success": "Profession '{}' created succesfully.".format(profession_saved, title)})


class SkillAPIView(APIView):

    def get(self, request):
        skills= Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response({"Skill": serializer.data})

    def post(self, request):
        serializer = SkillSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            skill_saved = serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        skill = get_object_or_404(Warrior, pk=pk)
        serializer = SkillSerializer(skill, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        skill = get_object_or_404(Skill, pk=pk)
        try:
            skill.delete()
            return Response(status=200)
        except:
            return Response(status=400)


class SkillCreateView(APIView):

    def post(self, request):
        skill = request.data.get("skill")
        serializer = SkillSerializer(data=skill)

        if serializer.is_valid(raise_exception=True):
            skill_saved = serializer.save()

        return Response({"Success": "Skill '{}' created succesfully.".format(skill_saved.title)})


class WarriorCreateAPIView(generics.ListCreateAPIView):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()


class WarriorDestroyView(generics.DestroyAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer


class WarriorUpdateView(generics.UpdateAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer


class WarriorDetailsView(generics.RetrieveAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorNestedSerializer


class WarriorViewSet(viewsets.ModelViewSet):
    queryset = Warrior.objects.all()
    serializer_class = WarriorNestedSerializer

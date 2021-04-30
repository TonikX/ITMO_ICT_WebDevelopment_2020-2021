from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response

from .models import *
from .serializers import *


# class WarriorAPIView(APIView):
#     def get(self, request):
#         warriors = Warrior.objects.all()
#         serializer = WarriorSerializer(warriors, many=True)
#         return Response({"Warriors": serializer.data})

class WarriorListAPIView(generics.ListAPIView):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()


class ProfessionAPIView(APIView):
    def get(self, request):
        professions = Profession.objects.all()
        serializer = ProfessionSerializer(professions, many=True)
        return Response({"Professions": serializer.data})


class ProfessionCreateAPIView(generics.CreateAPIView):
    serializer_class = ProfessionCreateSerializer
    queryset = Profession.objects.all()

# class ProfessionCreateView(APIView):

#     def post(self, request):
#         profession = request.data.get("profession")
#         serializer = ProfessionCreateSerializer(data=profession)

#         if serializer.is_valid(raise_exception=True):
#             profession_saved = serializer.save()

#         return Response({"Success": "Profession '{}' created succesfully.".format(profession_saved.title)})


class SkillAPIView(APIView):
    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response({"Skills": serializer.data})


# class SkillCreateView(APIView):

#     def post(self, request):
#         skill = request.data.get("skill")
#         serializer = SkillCreateSerializer(data=skill)

#         if serializer.is_valid(raise_exception=True):
#             skill_saved = serializer.save()

#         return Response({"Success": "Skill '{}' created succesfully.".format(skill_saved.title)})


# practice 3.1 last part


class WarriorCreateAPIView(generics.CreateAPIView):
    serializer_class = WarriorCreateSerializer


class SkillCreateAPIView(generics.CreateAPIView):
    serializer_class = SkillCreateSerializer


class SkillOfWarriorCreateAPIView(generics.CreateAPIView):
    serializer_class = SkillOfWarriorSerializer


class SkillOfWarriorListAPIView(generics.ListAPIView):
    serializer_class = SkillOfWarriorSerializer
    queryset = SkillOfWarrior.objects.all()

# удаление воина по id


class WarriorDestroyAPIView(generics.DestroyAPIView):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()
    lookup_field = 'id'

# редактирование информации о воине


class WarriorUpdateAPIView(generics.RetrieveUpdateAPIView):
    # generics.UpdateAPIView показывает пустые поля, не понятно, что за объект меняешь
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()

# вывод полной информации о воине


class WarriorRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = WarriorRetrieveSerializer
    queryset = Warrior.objects.all()

# воины и скиллы


class WarriorSkillListAPIView(generics.ListAPIView):
    serializer_class = WarriorSkillSerializer
    queryset = Warrior.objects.all()

# воины и профессии


class WarriorProfessionListAPIView(generics.ListAPIView):
    serializer_class = WarriorProfessionSerializer
    queryset = Warrior.objects.all()

from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
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


class ProfessionAPIView(APIView):

    def get(self, request):
        profession = Profession.objects.all()
        serializer = ProfessionSerializer(profession, many=True)
        return Response({"Profession": serializer.data})


# Задание 1: Реализовать ендпоинты для добавления и просмотра скилов +

class SkillCreateView(APIView):

    def post(self, request):
        skill = request.data.get("skill")
        serializer = SkillCreateSerializer(data=skill)

        if serializer.is_valid(raise_exception=True):
            skill_saved = serializer.save()

        return Response({"Success": "Skill '{}' created succesfully.".format(skill_saved.title)})


class SkillAPIView(APIView):

    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response({"Skills": serializer.data})


# Задание 2.
# Реализовать ендпоинты:
# 1. Вывод полной информации о всех войнах и их профессиях (в одном запросе)
class WarriorsProfessionsAPIView(generics.ListAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorProfessionSerializer


# 2. Вывод полной информации о всех войнах и их скилах (в одном запросе)
class WarriorsSkillsAllAPIView(generics.ListAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSkillSerializer


# 3. Вывод полной информации о войне (по id), его профессиях и скилах
class WarriorProfessionSkillAPIView(generics.RetrieveUpdateAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorRelatedSerializer


# 4. Удаление война по id
class WarriorDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorRelatedSerializer


# 5. Редактирование информации о войне
class WarriorUpdateAPIView(generics.UpdateAPIView):
    serializer_class = WarriorNestedSerializer
    queryset = Warrior.objects.all()
    lookup_field = 'pk'

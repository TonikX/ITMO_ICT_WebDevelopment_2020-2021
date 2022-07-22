from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from .models import Warrior, Skill, SkillOfWarrior
from .serializers import WarriorSerializer, ProfessionCreateSerializer, \
                         SkillSerializer, SkillCreateSerializer,\
                         WarriorRelatedProfessionSerializer,\
                         WarriorRelatedSkillSerializer, WarriorFullSerializer, SkillOfWarriorSerializer


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

        return Response({"Success": "Profession '{}' created successfully".format(profession_saved.title)})


class SkillAPIView(APIView):

    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response({"Skills ": serializer.data})


class SkillCreateView(APIView):

    def post(self, request):
        skill = request.data.get("skill")
        serializer = SkillCreateSerializer(data=skill)

        if serializer.is_valid(raise_exception=True):
            skill_saved = serializer.save()

        return Response({"Success": "Skill '{}' created successfully".format(skill_saved.title)})


class WarriorProfessionListAPIView(generics.ListAPIView):

    serializer_class = WarriorRelatedProfessionSerializer
    queryset = Warrior.objects.all()


class WarriorSkillListAPIView(generics.ListAPIView):

    serializer_class = WarriorRelatedSkillSerializer
    queryset = Warrior.objects.all()


class SingleWarriorAPIView(generics.RetrieveAPIView):

    serializer_class = WarriorFullSerializer
    queryset = Warrior.objects.all()


class DeleteWarriorAPIView(generics.DestroyAPIView):

    queryset = Warrior.objects.all()


class EditWarriorAPIView(generics.UpdateAPIView):

    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()


class EditWarriorSkillAPIView(generics.UpdateAPIView):

    serializer_class = SkillOfWarriorSerializer
    queryset = SkillOfWarrior.objects.all()
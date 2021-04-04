from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from warriors_app.serializers import *


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

       return Response({"Success": "Profession '{}' created successfully.".format(profession_saved.title)})


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

       return Response({"Success": "Skill '{}' created successfully.".format(skill_saved.title)})


class WarriorProfView(APIView):
   def get(self, request):
       war_prof = Warrior.objects.all()
       serializer = WarriorProfSerializer(war_prof, many=True)
       return Response({"Warriors and their profs": serializer.data})


class WarriorSkillView(APIView):
   def get(self, request):
       war_skill = Warrior.objects.all()
       serializer = WarriorSkillSerializer(war_skill, many=True)
       return Response({"Warriors and their skills": serializer.data})


class WarriorInfoView(generics.RetrieveAPIView):
    serializer_class = WarriorInfoSerializer
    queryset = Warrior.objects.all()


class WarriorEditView(generics.UpdateAPIView):
    serializer_class = WarriorInfoSerializer
    queryset = Warrior.objects.all()
    lookup_field = 'pk'


class WarriorDeleteView(generics.DestroyAPIView):
    serializer_class = WarriorInfoSerializer
    queryset = Warrior.objects.all()
    lookup_field = 'pk'


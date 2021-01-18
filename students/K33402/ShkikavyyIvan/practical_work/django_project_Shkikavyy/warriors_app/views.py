from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from warriors_app.serializer import *


class WarriorAPIView(APIView):
    def get(self, request):
        warriors = Warrior.objects.all()
        serializer = WarriorSerializer(warriors, many=True)
        return Response({"Warriors": serializer.data})

    def post(self, request):
        warrior = request.data.get("warrior")
        serializer = WarriorSerializer(data=warrior)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response({"Success": "Created succesfully."})


class ProfessionCreateView(APIView):
    def post(self, request):
        profession = request.data.get("profession")
        serializer = ProfessionSerializer(data=profession)

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


class GetSkillAPIView(APIView):
    def get(self, request):
        skill = Skill.objects.all()
        serializer = SkillSerializer(skill, many=True)
        return Response({"Skill": serializer.data})


class WarriorListAPIView(generics.ListAPIView):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()


class ProfessionCreateAPIView(generics.CreateAPIView):
    serializer_class = ProfessionSerializer
    queryset = Profession.objects.all()


class WarriorCreateAPIView(generics.CreateAPIView):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()


class SkillGenericCreateAPIView(generics.CreateAPIView):
    serializer_class = SkillSerializer
    queryset = Skill.objects.all()


class SkillOfWarriorCreateAPIView(generics.CreateAPIView):
    serializer_class = SkillOfWarriorSerializer
    queryset = SkillOfWarrior.objects.all()


class WarriorsSkills(APIView):
    def get(self, request):
        skill = Warrior.objects.all()
        serializer = WarriorSkillsSerializer(skill, many=True)
        return Response({"Skill": serializer.data})


class WarriorsProfession(APIView):
    def get(self, request):
        prof = Warrior.objects.all()
        serializer = WarriorProfSerializer(prof, many=True)
        return Response({"Professions": serializer.data})


class OneWarriorAPIView(generics.RetrieveAPIView):
    serializer_class = OneWarriorSerializer
    queryset = Warrior.objects.all()


class OneWarriorUpdateAPIView(generics.UpdateAPIView):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()
    lookup_field = 'pk'
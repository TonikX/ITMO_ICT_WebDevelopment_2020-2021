from rest_framework.views import *
from rest_framework.generics import *
from .models import Warrior, Skill, Profession
from .serializers import *


class WarriorAPIView(APIView):

    def get(self, request):
        warriors = Warrior.objects.all()
        serializer = WarriorSerializer(warriors, many=True)

        return Response({"Warriors": serializer.data})

    def post(self, request):
        warrior = request.data.get('warrior')
        serializer = WarriorSerializer(data=warrior)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response({"status": "ok"})


class CreateSkills(APIView):

    def post(self, request):
        skill = request.data.get('skill')
        serializer = SkillSerializer(data=skill)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response({"status": "ok"})


class GetSkills(APIView):

    def get(self, request):
        skill = Skill.objects.all()
        serializer = SkillSerializer(skill, many=True)

        return Response({"Skills": serializer.data})


class WarriorListAPIView(ListAPIView):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()


class WarriorCreateAPIView(CreateAPIView):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()


class ProfessionCreateAPIView(CreateAPIView):
    serializer_class = ProfessionSerializer
    queryset = Profession.objects.all()


class WarriorWithJobsAPIView(ListAPIView):
    serializer_class = WarriorWithJobsSerializer
    queryset = Warrior.objects.all()


class SkillOfWarriorCreateAPIView(ListCreateAPIView):
    serializer_class = SkillOfWarriorSerializer
    queryset = SkillOfWarrior.objects.all()


class WarriorWithSkillsAPIView(ListAPIView):
    serializer_class = WarriorWithSkillsSerializer
    queryset = Warrior.objects.all()


class WarriorSingleAPIView(RetrieveAPIView):
    serializer_class = WarriorFullSerializer
    queryset = Warrior.objects.all()
    lookup_field = 'pk'


class WarriorUpdateAPIView(UpdateAPIView):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()
    lookup_field = 'pk'










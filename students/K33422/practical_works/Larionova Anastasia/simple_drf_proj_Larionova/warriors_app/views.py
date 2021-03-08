from rest_framework import status
from rest_framework.views import APIView, Response
from django.shortcuts import get_object_or_404
from .serializers import *


class WarriorListAPIView(generics.ListAPIView):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()

    def put(self, request, pk=None):
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


class SingleWarriorAPIView(generics.RetrieveAPIView):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()


class SkillAPIView(APIView):
    def get(self, request):
        skill = Skill.objects.all()
        serializer = SkillSerializer(skill, many=True)
        return Response({"Skills": serializer.data})


class SkillCreateView(APIView):
    def post(self, request):
        skill = request.data.get("skill")
        serializer = SkillCreateSerializer(data=skill)

        if serializer.is_valid(raise_exception=True):
            skill_saved = serializer.save()

        return Response({"Success": "Skill '{}' created successfully.".format(skill_saved.title)})


class ProfessionAPIView(generics.ListAPIView):
    serializer_class = ProfessionRelatedSerializer
    queryset = Warrior.objects.all()


class SkillOfWarriorAPIView(generics.ListAPIView):
    serializer_class = SkillRelatedSerializer
    queryset = Warrior.objects.all()

    def put(self, request, pk=None):
        warrior = get_object_or_404(Warrior, pk=pk)
        serializer = SkillRelatedSerializer(warrior, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from rest_framework import status
from rest_framework.views import APIView, Response
from django.shortcuts import get_object_or_404
from .serializers import *
from .models import *


class WarriorAPIView(APIView):
    def get(self, request):
        warriors = Warrior.objects.all()
        serializer = WarriorNestedSerializer(warriors, many=True)
        return Response({"Warriors": serializer.data})


class WarriorCreateAPIView(generics.CreateAPIView):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()


# def put(self, request, pk=None):
#     warrior = get_object_or_404(Warrior, pk=pk)
#     serializer = WarriorSerializer(warrior, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# class ProfessionCreateView(APIView):
#     def post(self, request):
#         profession = request.data.get("profession")
#         serializer = ProfessionSerializer(data=profession)
#         if serializer.is_valid(raise_exception=True):
#             profession_saved = serializer.save()
#         return Response({"Success": "Profession '{}' created succesfully.".format(profession_saved.title)})


class WarriorListAPIView(generics.ListAPIView):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()


class ProfessionCreateAPIView(generics.CreateAPIView):
    serializer_class = ProfessionSerializer
    queryset = Profession.objects.all()


class SkillsCreateView(APIView):

    def post(self, request):
        skill = request.data.get("skill")
        serializer = SkillSerializer(data=skill)

        if serializer.is_valid(raise_exception=True):
            skill_saved = serializer.save()

        return Response({"Success": "skill '{}' created succesfully.".format(skill_saved.title)})


class WarriorDestroyView(generics.DestroyAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer


class WarriorUpdateView(generics.UpdateAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer


class SingleWarriorAPIView(generics.RetrieveAPIView):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()

from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework import generics
from django.shortcuts import get_object_or_404

from .models import *
from .serializers import *


class WarriorAPIView(APIView):
  def get(self, request):
    skills = Skill.objects.all()
    serializer = SkillRelatedSerializer(skills, many=True)
    return Response({'Skills': serializer.data})

  def post(self, request):
    serializer = WarriorSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      article_saved = serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

class WarriorCreateAPIView(generics.ListCreateAPIView):
  serializer_class = WarriorSerializer
  queryset = Warrior.objects.all()

class WarriorDestroyView(generics.DestroyAPIView):
  queryset = Warrior.objects.all()
  serializer_class = WarriorSerializer

class WarriorUpdateView(generics.UpdateAPIView):
  queryset = Warrior.objects.all()
  serializer_class = WarriorSerializer

# class WarriorDetailsView(generics.RetreiveAPIView):
#   queryset = Warrior.objects.all()
#   serializer_class = WarriorSerializer


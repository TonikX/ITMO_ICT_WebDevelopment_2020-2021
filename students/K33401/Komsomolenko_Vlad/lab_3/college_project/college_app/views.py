from django.shortcuts import render
from rest_framework.views import APIView, Response
from .serializers import *
import requests
from rest_framework import generics

class DisciplineCreateAPIView(generics.CreateAPIView):
   serializer_class = DisciplineSerializer
   queryset = Discipline.objects.all()

class DisciplineAPIView(generics.ListAPIView):
   serializer_class = DisciplineSerializer
   queryset = Discipline.objects.all()

class PairCreateAPIView(generics.CreateAPIView):
   serializer_class = PairSerializer
   queryset = Pair.objects.all()

class PairAPIView(generics.ListAPIView):
   serializer_class = PairSerializer
   queryset = Pair.objects.all()

class TeacherCreateAPIView(generics.CreateAPIView):
   serializer_class = TeacherSerializer
   queryset = Teacher.objects.all()

class TeacherAPIView(generics.ListAPIView):
   serializer_class = TeacherSerializer
   queryset = Teacher.objects.all()

class TeacherDisciplineView(generics.CreateAPIView):
   serializer_class = TeacherDisciplineNestedSerializer
   queryset = DisciplineOfTeacher.objects.all()

class StudentCreateAPIView(generics.CreateAPIView):
   serializer_class = StudentSerializer
   queryset = Student.objects.all()

class StudentAPIView(generics.ListAPIView):
   serializer_class = StudentSerializer
   queryset = Student.objects.all()

class PairCreateAPIView(generics.CreateAPIView):
   serializer_class = PairSerializer
   queryset = Pair.objects.all()

class PairAPIView(generics.ListAPIView):
   serializer_class = PairSerializer
   queryset = Pair.objects.all()

class ScheduleCreateAPIView(generics.CreateAPIView):
   serializer_class = ScheduleSerializer
   queryset = Schedule.objects.all()

class ScheduleAPIView(generics.ListAPIView):
   serializer_class = ScheduleSerializer
   queryset = Schedule.objects.all()

class PairScheduleView(generics.CreateAPIView):
   serializer_class = PairScheduleNestedSerializer
   queryset = PairOfSchedule.objects.all()

class MarkCreateAPIView(generics.CreateAPIView):
   serializer_class = MarkSerializer
   queryset = Mark.objects.all()

class MarkAPIView(generics.ListAPIView):
   serializer_class = MarkSerializer
   queryset = Mark.objects.all()

class StudentMarkAPIView(generics.CreateAPIView):
   serializer_class = StudentMarkSerializer
   queryset = MarkOfStudent.objects.all()

class StudentMarkUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
   serializer_class = StudentMarkSerializer
   queryset = MarkOfStudent.objects.all()

class StudentUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
   serializer_class = StudentSerializer
   queryset = Student.objects.all()

class TeacherUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
   serializer_class = TeacherSerializer
   queryset = Teacher.objects.all()


class UserProfileListCreateView(generics.ListCreateAPIView):
   queryset = userProfile.objects.all()
   serializer_class = userProfileSerializer
   permission_classes = []

   def perform_create(self, serializer):
      user = self.request.user
      serializer.save(user=user)


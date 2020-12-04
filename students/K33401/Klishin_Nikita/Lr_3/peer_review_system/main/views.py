from accounts.models import CustomUser, StudentProfile
from django.http.response import Http404
from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import (
	Task, 
	TaskExecutor,
	StudentsClass
)

from main.serializers import (
	StudentsClassDetailSerializer, 
	StudentsClassSerializer, 
	TaskSerializer,
)

from accounts.serializers import (
	StudentSerializer, UserSerializer,
)


# сериализаторы для задач
class TaskListView(generics.ListCreateAPIView):
	queryset = Task.objects.all()
	serializer_class = TaskSerializer

class TaskDetialView(generics.RetrieveAPIView):
	queryset = Task.objects.all()
	serializer_class = TaskSerializer

class TaskExecutorsListView(APIView):

	def get(self, request, pk, format=None):
		currentTask = Task.objects.get(pk=pk)
		executors = currentTask.executors.all()

		serializer = UserSerializer(executors, many=True)

		return Response(serializer.data)


class MyExecutionTaskListView(generics.ListAPIView):

	permission_classes = [IsAuthenticated]

	def get_queryset(self):
		user = self.request.user

		return user.tasks_to_execute.all()
	
	serializer_class = TaskSerializer

class MyInspectionTaskListView(generics.ListAPIView):

	permission_classes = [IsAuthenticated]

	def get_queryset(self):
		user = self.request.user

		return user.tasks_to_inspect.all()
	
	serializer_class = TaskSerializer


class StudentsClassListView(generics.ListAPIView):

	queryset = StudentsClass.objects.all()
	serializer_class = StudentsClassSerializer


class StudentsClassDetailView(APIView):

	def get_object(self, pk):
		try:
			return StudentsClass.objects.get(pk=pk)
		except StudentsClass.DoesNotExist:
			raise Http404
	
	def get(self, request, pk, format=None):
		studentClass = self.get_object(pk=pk)
		studentsInClass = StudentProfile.objects.filter(student_class=studentClass).all()

		classSerializer = StudentsClassDetailSerializer(studentClass)
		studentSerializer = StudentSerializer(studentsInClass, many=True)

		return Response({
			"Main info": classSerializer.data,
			"Students": studentSerializer.data
		})




class StudentsInClassListView(generics.ListAPIView):

	def get_queryset(self):
		pass

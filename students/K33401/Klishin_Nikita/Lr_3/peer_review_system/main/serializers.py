from accounts.models import StudentProfile
from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers

from .models import (
	Task,
	StudentsClass
)


class TaskSerializer(serializers.ModelSerializer):

	class Meta:
		model = Task
		fields = "__all__"


# сериализаторы для классов
class StudentsClassSerializer(serializers.ModelSerializer):

	class Meta:
		model = StudentsClass
		fields = "__all__"


class StudentsClassDetailSerializer(serializers.Serializer):
	title = serializers.CharField(max_length=140)


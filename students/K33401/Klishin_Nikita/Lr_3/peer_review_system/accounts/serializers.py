from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
# from django.contrib.auth.models import User

from .models import (
	CustomUser,
	StudentProfile,
)


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomUser
		fields = ["email", 'is_teacher']
		ref_name = "Custom user"

class UserRegistrationSerializer(UserCreateSerializer):

	class Meta(UserCreateSerializer.Meta):
		fields = ('email', 'password', 'is_teacher')


class StudentSerializer(serializers.ModelSerializer):
	user = UserSerializer()
	class Meta:
		model = StudentProfile
		fields = ["id", "user"]


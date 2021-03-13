from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import *


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = "__all__"


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = "__all__"


class CleaningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cleaning
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
            password=make_password(validated_data['password']),
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

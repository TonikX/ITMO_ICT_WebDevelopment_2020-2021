from rest_framework import serializers
from .models import *

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = "__all__"

class StaffCleaningSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffCleaning
        fields = "__all__"

class CleaningParamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CleaningParams
        fields = "__all__"

class CleaningParamsPartedSerializer(serializers.ModelSerializer):
    class Meta:
        model = CleaningParams
        fields = ["day", "floor"]

class StaffSerializer(serializers.ModelSerializer):
    cleaning = CleaningParamsPartedSerializer(many=True, read_only=True)
    class Meta:
        model = Staff
        fields = "__all__"

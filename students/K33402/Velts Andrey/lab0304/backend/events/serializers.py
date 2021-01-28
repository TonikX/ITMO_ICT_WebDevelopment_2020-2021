from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ("id", "title", "description", "start_date", "end_date", "category")
        read_only_fields = fields


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ("id", "title", "description", "category", "start_date", "end_date")
        read_only_fields = fields

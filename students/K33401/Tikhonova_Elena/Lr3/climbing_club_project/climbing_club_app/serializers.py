from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class ClimberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'address', 'club']


class PeakSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peak
        fields = ['name', 'country', 'height',
                  'climbing_duration', 'route_description']


class ClimbingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Climbing
        fields = ['start_time', 'finish_time',
                  'peak', 'participants', 'information']


class ParticipationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participation
        fields = ['climbing', 'participant']


class EmergencySituationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergencySituation
        fields = ['climbing', 'person', 'description']


class CountClimbersSerializer(serializers.ModelSerializer):
    climbings_on_peak = serializers.IntegerField()

    class Meta:
        model = Person
        fields = ['first_name', 'last_name',
                  'address', 'club', 'climbings_on_peak']

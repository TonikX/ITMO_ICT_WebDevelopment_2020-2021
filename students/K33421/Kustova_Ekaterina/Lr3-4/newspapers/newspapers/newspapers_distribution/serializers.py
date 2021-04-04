from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class NewspaperSerializer(serializers.ModelSerializer):

  class Meta:
     model = Newspaper
     fields = "__all__"


class PrinterySerializer(serializers.ModelSerializer):

  class Meta:
     model = Printery
     fields = "__all__"

class PostOfficeSerializer(serializers.ModelSerializer):

  class Meta:
     model = PostOffice
     fields = "__all__"

class NewspapersPartySerializer(serializers.ModelSerializer):

  class Meta:
     model = NewspapersParty
     fields = "__all__"

class PrintSerializer(serializers.ModelSerializer):
  class Meta:
      model = Print
      fields = "__all__"


class DistributionReportSerializer(serializers.ModelSerializer):
  class Meta:
      model = DistributionReport
      fields = "__all__"


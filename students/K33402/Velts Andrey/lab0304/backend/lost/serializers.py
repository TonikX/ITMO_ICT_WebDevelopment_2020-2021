from rest_framework import serializers
from .models import Lost
from home.serializers import ThumbnailSerializer


class LostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lost
        fields = (
            "id",
            "name",
            "age",
            "city",
            "gender",
            "description",
            "location",
            "contacts",
            "image",
        )

from rest_framework import serializers
from .models import Pet
from home.serializers import ThumbnailSerializer


class PetsSerializer(serializers.ModelSerializer):
    image = ThumbnailSerializer("pet")

    class Meta:
        model = Pet
        fields = ("id", "name", "age", "gender", "image")
        read_only_fields = fields

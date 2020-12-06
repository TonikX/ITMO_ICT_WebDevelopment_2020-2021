from rest_framework import serializers
from .models import Charity
from home.serializers import ThumbnailSerializer


class CharitySerializer(serializers.ModelSerializer):
    image = ThumbnailSerializer("pet")

    class Meta:
        model = Charity
        fields = (
            "id",
            "title",
            "description",
            "goal_money",
            "current_money",
            "donation_times",
            "image",
        )
        read_only_fields = fields

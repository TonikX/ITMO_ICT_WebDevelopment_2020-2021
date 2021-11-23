from rest_framework import serializers
from .models import Item


class ItemsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ("id", "name", "type", "description")
        read_only_fields = fields

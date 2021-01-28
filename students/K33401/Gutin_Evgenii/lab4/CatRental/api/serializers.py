from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *


class CatSerializer(ModelSerializer):

    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Cat
        fields = "__all__"


class CatToOrderSerializer(ModelSerializer):

    class Meta:
        model = CatToOrder
        fields = "__all__"


class OrderFullSerializer(ModelSerializer):

    cats = CatSerializer(many=True)

    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Order
        fields = "__all__"


class OrderSerializer(ModelSerializer):

    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Order
        fields = "__all__"


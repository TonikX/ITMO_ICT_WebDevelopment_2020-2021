from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model


class CarSerializer(ModelSerializer):

    class Meta:
        model = Car
        fields = "__all__"


class CarToOrderSerializer(ModelSerializer):

    class Meta:
        model = CarToOrder
        fields = "__all__"


class OrderFullSerializer(ModelSerializer):

    cars = CarSerializer(many=True)

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


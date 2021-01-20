from rest_framework import serializers

from .models import *


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = "__all__"


class OrderFullSerializer(serializers.ModelSerializer):

    person = serializers.HiddenField(default=serializers.CurrentUserDefault())
    pizzas = PizzaSerializer(many=True)

    class Meta:
        model = Order
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):

    person = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Order
        fields = "__all__"


class OrderedPizzasSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderedPizzas
        fields = "__all__"

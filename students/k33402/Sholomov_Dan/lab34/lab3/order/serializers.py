from rest_framework import serializers
from .models import Order, OrderedItem


class OrdersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ("id", "person", "items", "description")
        read_only_fields = fields


class OrderedItemsSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderedItem
        fields = ("id", "item", "order", "amount")
        read_only_fields = fields

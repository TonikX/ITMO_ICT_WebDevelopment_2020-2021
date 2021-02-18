from rest_framework import viewsets
from .serializers import OrdersSerializer, OrderedItemsSerializer
from .models import Order, OrderedItem


class OrdersViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = OrdersSerializer
    queryset = Order.objects.all()
    permission_classes = []


class OrderedItemsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = OrderedItemsSerializer
    queryset = OrderedItem.objects.all()
    permission_classes = []

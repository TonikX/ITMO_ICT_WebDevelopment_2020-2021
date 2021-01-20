from django.shortcuts import render
from rest_framework import authentication, permissions

from .serializers import *
from rest_framework.generics import *

# Create your views here.


class IsOwner(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user == Order.objects.get(pk=view.kwargs('pk')).person


class OrderIsFromOwner(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user == Order.objects.get(pk=request.data.get('order')).person


class PizzasListAPIView(ListAPIView):

    permission_classes = [permissions.IsAuthenticated]

    serializer_class = PizzaSerializer
    queryset = Pizza.objects.all()


class PizzasCreateAPIView(CreateAPIView):

    permission_classes = [permissions.IsAdminUser]

    serializer_class = PizzaSerializer
    queryset = Pizza.objects.all()


class PizzasRetrieveAPIView(RetrieveAPIView):

    permission_classes = [permissions.IsAuthenticated]

    serializer_class = PizzaSerializer
    queryset = Pizza.objects.all()
    lookup_field = 'pk'


class PizzasUpdateAPIView(UpdateAPIView):

    permission_classes = [permissions.IsAdminUser]

    serializer_class = PizzaSerializer
    queryset = Pizza.objects.all()
    lookup_field = 'pk'


class PizzasDeleteAPIView(DestroyAPIView):

    permission_classes = [permissions.IsAdminUser]

    serializer_class = PizzaSerializer
    queryset = Pizza.objects.all()
    lookup_field = 'pk'


class OrderListAPIView(ListAPIView):

    permission_classes = [permissions.IsAuthenticated]

    serializer_class = OrderFullSerializer

    def get_queryset(self):
        return Order.objects.filter(person=self.request.user)


class OrderCreateAPIView(CreateAPIView):

    permission_classes = [permissions.IsAuthenticated]

    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderRetrieveAPIView(RetrieveAPIView):

    permission_classes = [IsOwner]

    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    lookup_field = 'pk'


class OrderUpdateAPIView(UpdateAPIView):

    permission_classes = [IsOwner]

    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    lookup_field = 'pk'


class OrderDeleteAPIView(DestroyAPIView):

    permission_classes = [IsOwner]

    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    lookup_field = 'pk'


class OrderedPizzasListAPIView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = OrderedPizzasSerializer
    queryset = OrderedPizzas.objects.all()


class OrderedPizzasCreateAPIView(CreateAPIView):
    permission_classes = [OrderIsFromOwner]

    serializer_class = OrderedPizzasSerializer
    queryset = OrderedPizzas.objects.all()


class OrderedPizzasRetrieveAPIView(RetrieveAPIView):
    permission_classes = [OrderIsFromOwner]

    serializer_class = OrderedPizzasSerializer
    queryset = OrderedPizzas.objects.all()
    lookup_field = 'pk'


class OrderedPizzasUpdateAPIView(UpdateAPIView):
    permission_classes = [OrderIsFromOwner]

    serializer_class = OrderedPizzasSerializer
    queryset = OrderedPizzas.objects.all()
    lookup_field = 'pk'


class OrderedPizzasDeleteAPIView(DestroyAPIView):
    permission_classes = [OrderIsFromOwner]

    serializer_class = OrderedPizzasSerializer
    queryset = OrderedPizzas.objects.all()
    lookup_field = 'pk'


from rest_framework.generics import *
from rest_framework import permissions
from .serializers import *

# ---------- custom permissions --------- #


class IsOrderOwner(permissions.BasePermission):

    def has_permission(self, request, view):

        return request.user == Order.objects.get(pk=view.kwargs['pk']).user


class IsOrderOwnerCarToOrder(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user == Order.objects.get(pk=request.data.get('order')).user


#  -------------- Cars --------------- #


class CarsAPIView(ListAPIView):

    permission_classes = [permissions.AllowAny]

    serializer_class = CarSerializer
    queryset = Car.objects.all()


class CarsCreateAPIView(CreateAPIView):

    permission_classes = [permissions.IsAdminUser]

    serializer_class = CarSerializer
    queryset = Car.objects.all()


class CarAPIView(RetrieveAPIView):

    permission_classes = [permissions.AllowAny]

    serializer_class = CarSerializer
    queryset = Car.objects.all()
    lookup_field = 'pk'


class CarUpdateAPIView(UpdateAPIView):

    permission_classes = [permissions.IsAdminUser]

    serializer_class = CarSerializer
    queryset = Car.objects.all()
    lookup_field = 'pk'


class CarDeleteAPIView(DestroyAPIView):

    permission_classes = [permissions.IsAdminUser]

    serializer_class = CarSerializer
    queryset = Car.objects.all()
    lookup_field = 'pk'


#  -------------- orders --------------- #


class OrdersAPIView(ListAPIView):

    permission_classes = [permissions.IsAuthenticated]

    serializer_class = OrderFullSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class OrdersCreateAPIView(CreateAPIView):

    permission_classes = [permissions.IsAuthenticated]

    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderAPIView(RetrieveAPIView):

    permission_classes = [IsOrderOwner]

    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    lookup_field = 'pk'


class OrderUpdateAPIView(UpdateAPIView):

    permission_classes = [IsOrderOwner]

    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    lookup_field = 'pk'


class OrderDeleteAPIView(DestroyAPIView):

    permission_classes = [IsOrderOwner]

    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    lookup_field = 'pk'


# ------------ Car to order ----------- #

class CarToOrderCreateAPIView(CreateAPIView):

    permission_classes = [IsOrderOwnerCarToOrder]

    serializer_class = CarToOrderSerializer
    queryset = CarToOrder.objects.all()


class CarToOrderAPIView(RetrieveAPIView):

    permission_classes = [IsOrderOwnerCarToOrder]

    serializer_class = CarToOrderSerializer
    queryset = CarToOrder.objects.all()
    lookup_field = 'pk'


class CarToOrderUpdateAPIView(UpdateAPIView):

    permission_classes = [IsOrderOwnerCarToOrder]

    serializer_class = CarToOrderSerializer
    queryset = CarToOrder.objects.all()
    lookup_field = 'pk'


class CarToOrderDeleteAPIView(DestroyAPIView):

    permission_classes = [IsOrderOwnerCarToOrder]

    serializer_class = CarToOrderSerializer
    queryset = CarToOrder.objects.all()
    lookup_field = 'pk'

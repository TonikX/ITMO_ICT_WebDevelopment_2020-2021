from rest_framework.generics import *
from rest_framework import permissions
from .serializers import *

# ---------- custom permissions --------- #


class IsOrderOwner(permissions.BasePermission):

    def has_permission(self, request, view):

        return request.user == Order.objects.get(pk=view.kwargs['pk']).user


class IsOrderOwnerCatToOrder(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user == Order.objects.get(pk=request.data.get('order')).user


#  -------------- cats --------------- #


class CatsAPIView(ListAPIView):

    permission_classes = [permissions.AllowAny]

    serializer_class = CatSerializer
    queryset = Cat.objects.all()


class OwnerCatsAPIView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = CatSerializer

    def get_queryset(self):
        return Cat.objects.filter(user=self.request.user)


class CatsCreateAPIView(CreateAPIView):

    permission_classes = [permissions.IsAuthenticated]

    serializer_class = CatSerializer
    queryset = Cat.objects.all()


class CatAPIView(RetrieveAPIView):

    permission_classes = [permissions.AllowAny]

    serializer_class = CatSerializer
    queryset = Cat.objects.all()
    lookup_field = 'pk'


class CatUpdateAPIView(UpdateAPIView):

    permission_classes = [permissions.IsAdminUser]

    serializer_class = CatSerializer
    queryset = Cat.objects.all()
    lookup_field = 'pk'


class CatDeleteAPIView(DestroyAPIView):

    permission_classes = [permissions.IsCatOwner]

    serializer_class = CatSerializer
    queryset = Cat.objects.all()
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


# ------------ cat to order ----------- #

class CatToOrderCreateAPIView(CreateAPIView):

    permission_classes = [IsOrderOwnerCatToOrder]

    serializer_class = CatToOrderSerializer
    queryset = CatToOrder.objects.all()


class CatToOrderAPIView(RetrieveAPIView):

    permission_classes = [IsOrderOwnerCatToOrder]

    serializer_class = CatToOrderSerializer
    queryset = CatToOrder.objects.all()
    lookup_field = 'pk'


class CatToOrderUpdateAPIView(UpdateAPIView):

    permission_classes = [IsOrderOwnerCatToOrder]

    serializer_class = CatToOrderSerializer
    queryset = CatToOrder.objects.all()
    lookup_field = 'pk'


class CatToOrderDeleteAPIView(DestroyAPIView):

    permission_classes = [IsOrderOwnerCatToOrder]

    serializer_class = CatToOrderSerializer
    queryset = CatToOrder.objects.all()
    lookup_field = 'pk'

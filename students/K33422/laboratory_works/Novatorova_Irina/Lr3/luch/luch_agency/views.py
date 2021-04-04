from .serializers import *
from rest_framework import generics
# Create your views here.


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserEditAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ApplicationNestedAPIView(generics.ListAPIView):
    serializer_class = ApplicationNestedSerializer

    def get_queryset(self):
        queryset = Application.objects.all()

        params = self.request.query_params

        client = params.get('client', None)

        if client:
            queryset = queryset.filter(client=client)

        return queryset


class ApplicationEditAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class ApplicationCreateAPIView(generics.CreateAPIView):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()


class ClientListAPIView(generics.ListAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class ClientEditAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientCreateAPIView(generics.CreateAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class ManufactoryNestedAPIView(generics.ListAPIView):
    serializer_class = ManufactoryNestedSerializer
    queryset = Manufactory.objects.all()


class ManufactoryEditAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manufactory.objects.all()
    serializer_class = ManufactorySerializer


class PaymentOrderNestedAPIView(generics.ListAPIView):
    serializer_class = PaymentOrderNestedSerializer

    def get_queryset(self):
        queryset = Payment_order.objects.all()

        params = self.request.query_params

        client = params.get('client', None)

        if client:
            queryset = queryset.filter(client=client)

        return queryset


class ServiceListAPIView(generics.ListAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()


class ServiceEditAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceCreateAPIView(generics.CreateAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()


class MaterialListAPIView(generics.ListAPIView):
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()


class MaterialEditAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


class MaterialCreateAPIView(generics.CreateAPIView):
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()


class WorkerListAPIView(generics.ListAPIView):
    serializer_class = WorkerSerializer
    queryset = Worker.objects.all()


class WorkerEditAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer


class WorkerCreateAPIView(generics.CreateAPIView):
    serializer_class = WorkerSerializer
    queryset = Worker.objects.all()


class ApplicationListNestedAPIView(generics.ListAPIView):
    serializer_class = ApplicationListNestedSerializer

    def get_queryset(self):
        queryset = Application_list.objects.all()

        params = self.request.query_params

        worker = params.get('worker', None)

        if worker:
            queryset = queryset.filter(worker=worker)

        return queryset





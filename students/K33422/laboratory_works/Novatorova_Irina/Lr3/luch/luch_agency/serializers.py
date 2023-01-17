from .models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = "__all__"


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class ManufactorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufactory
        fields = "__all__"


class MaterialSerializer(serializers.ModelSerializer):
    type_service = serializers.CharField(source="get_type_service_display", read_only=True)
    class Meta:
        model = Material
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):
    type_service = serializers.CharField(source="get_type_service_display", read_only=True)
    class Meta:
        model = Service
        fields = "__all__"


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = "__all__"



class ApplicationNestedSerializer(serializers.ModelSerializer):

    client = ClientSerializer()
    service = ServiceSerializer()

    status = serializers.CharField(source="get_status_display", read_only=True)

    class Meta:
        model = Application
        fields = "__all__"


class PaymentOrderNestedSerializer(serializers.ModelSerializer):

    application = ApplicationSerializer()
    client = ClientSerializer()
    service = ServiceSerializer()


    class Meta:
        model = Payment_order
        fields = "__all__"


class ManufactoryNestedSerializer(serializers.ModelSerializer):

    application = ApplicationSerializer()
    material = MaterialSerializer()
    service = ServiceSerializer()


    class Meta:
        model = Manufactory
        fields = "__all__"


class ApplicationListNestedSerializer(serializers.ModelSerializer):

    application = ApplicationSerializer()
    worker = WorkerSerializer()
    service = ServiceSerializer()


    class Meta:
        model = Application_list
        fields = "__all__"
from rest_framework import serializers
from .models import *


# Данные по врачам больницы
class DoctorViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "username", "fio", "speciality", "education", "work_years"


# Данные по кабинетам
class CabinetViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cabinet
        fields = "__all__"


# Данные по прайсам
class PriceViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = "__all__"


# Данные по пациенту
class PatientViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"


# Диагнозы
class DiagnosisViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnosis
        fields = "__all__"


# Расписание
class ScheduleNestedSerializer(serializers.ModelSerializer):
    id_doctor = DoctorViewSerializer()
    number_cabinet = CabinetViewSerializer()

    class Meta:
        model = Schedule
        fields = "__all__"


class ScheduleCreateSerializer(serializers.Serializer):
    id_doctor = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all())
    number_cabinet = serializers.PrimaryKeyRelatedField(queryset=Cabinet.objects.all())

    start_time = serializers.TimeField()
    end_time = serializers.TimeField()
    day = serializers.CharField(max_length=60)

    def create(self, validated_data):
        schedule = Schedule(**validated_data)
        schedule.save()
        return Schedule(**validated_data)


class ScheduleViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = "__all__"


# Медкарта
class MedcardDepthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medcard
        fields = "__all__"
        depth = 1


class MedcardCreateSerializer(serializers.Serializer):
    id_patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())
    id_diagnosis = serializers.PrimaryKeyRelatedField(queryset=Diagnosis.objects.all())

    start_date = serializers.DateField()
    status = serializers.CharField(max_length=60)

    def create(self, validated_data):
        medcard = Medcard(**validated_data)
        medcard.save()
        return Medcard(**validated_data)


class MedcardViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medcard
        fields = "__all__"


# Приём у врача
class MeetingNestedSerializer(serializers.ModelSerializer):
    id_patient = PatientViewSerializer()
    id_doctor = DoctorViewSerializer()
    id_price = PriceViewSerializer()

    class Meta:
        model = Meeting
        fields = "__all__"


class MeetingViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = "__all__"

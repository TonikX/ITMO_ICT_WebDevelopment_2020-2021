from rest_framework import status, generics
from .models import *
from .serializers import *


# Врач
class DoctorAPIView(generics.ListAPIView):
    serializer_class = DoctorViewSerializer
    queryset = Doctor.objects.all()


class DoctorCreateAPIView(generics.ListCreateAPIView):
    serializer_class = DoctorViewSerializer
    queryset = Doctor.objects.all()


class DoctorRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DoctorViewSerializer
    queryset = Doctor.objects.all()


# Кабинет
class CabinetAPIView(generics.ListAPIView):
    serializer_class = CabinetViewSerializer
    queryset = Cabinet.objects.all()


class CabinetCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CabinetViewSerializer
    queryset = Cabinet.objects.all()


class CabinetRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CabinetViewSerializer
    queryset = Cabinet.objects.all()


# Прейскурант
class PriceAPIView(generics.ListAPIView):
    serializer_class = PriceViewSerializer
    queryset = Price.objects.all()


class PriceCreateAPIView(generics.ListCreateAPIView):
    serializer_class = PriceViewSerializer
    queryset = Price.objects.all()


class PriceRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PriceViewSerializer
    queryset = Price.objects.all()


# Пациенты
class PatientAPIView(generics.ListAPIView):
    serializer_class = PatientViewSerializer
    queryset = Patient.objects.all()


class PatientCreateAPIView(generics.ListCreateAPIView):
    serializer_class = PatientViewSerializer
    queryset = Patient.objects.all()


class PatientRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PatientViewSerializer
    queryset = Patient.objects.all()


# Диагнозы
class DiagnosisAPIView(generics.ListAPIView):
    serializer_class = DiagnosisViewSerializer
    queryset = Diagnosis.objects.all()


class DiagnosisCreateAPIView(generics.ListCreateAPIView):
    serializer_class = DiagnosisViewSerializer
    queryset = Diagnosis.objects.all()


class DiagnosisRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DiagnosisViewSerializer
    queryset = Diagnosis.objects.all()


# Расписание
class ScheduleListAPIView(generics.ListAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleNestedSerializer


class ScheduleCreateAPIView(generics.CreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleCreateSerializer


class ScheduleRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleViewSerializer


# Медкарта
class MedcardListAPIView(generics.ListAPIView):
    queryset = Medcard.objects.all()
    serializer_class = MedcardDepthSerializer


class MedcardCreateAPIView(generics.CreateAPIView):
    queryset = Medcard.objects.all()
    serializer_class = MedcardCreateSerializer


class MedcardRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Medcard.objects.all()
    serializer_class = MedcardViewSerializer


# Приём
class MeetingDetailListAPIView(generics.ListAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingNestedSerializer


class MeetingCreateAPIView(generics.CreateAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingViewSerializer


class MeetingRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingViewSerializer


class MeetingListAPIView(generics.ListAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingViewSerializer
from django.urls import path
from .views import *

app_name = "hospital"

urlpatterns = [
    path('doctor/', DoctorAPIView.as_view()),
    path('doctor/create/', DoctorCreateAPIView.as_view()),
    path('doctor/<int:pk>/', DoctorRUDAPIView.as_view()),

    path('cabinet/', CabinetAPIView.as_view()),
    path('cabinet/create/', CabinetCreateAPIView.as_view()),
    path('cabinet/<int:pk>/', CabinetRUDAPIView.as_view()),

    path('price/', PriceAPIView.as_view()),
    path('price/create/', PriceCreateAPIView.as_view()),
    path('price/<int:pk>/', PriceRUDAPIView.as_view()),

    path('patient/', PatientAPIView.as_view()),
    path('patient/create/', PatientCreateAPIView.as_view()),
    path('patient/<int:pk>/', PatientRUDAPIView.as_view()),

    path('diagnosis/', DiagnosisAPIView.as_view()),
    path('diagnosis/create/', DiagnosisCreateAPIView.as_view()),
    path('diagnosis/<int:pk>/', DiagnosisRUDAPIView.as_view()),

    path('schedule/', ScheduleListAPIView.as_view()),
    path('schedule/create/', ScheduleCreateAPIView.as_view()),
    path('schedule/<int:pk>/', ScheduleRUDAPIView.as_view()),

    path('medcard/', MedcardListAPIView.as_view()),
    path('medcard/create/', MedcardCreateAPIView.as_view()),
    path('medcard/<int:pk>/', MedcardRUDAPIView.as_view()),

    path('meeting/', MeetingListAPIView.as_view()),
    path('meeting/detail/', MeetingDetailListAPIView.as_view()),
    path('meeting/create/', MeetingCreateAPIView.as_view()),
    path('meeting/<int:pk>/', MeetingRUDAPIView.as_view())
]
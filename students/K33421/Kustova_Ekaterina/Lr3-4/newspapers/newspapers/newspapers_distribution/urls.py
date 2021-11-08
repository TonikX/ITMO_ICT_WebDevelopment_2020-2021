from django.urls import path
from .views import *


app_name = "newspapers_distribution"


urlpatterns = [
   path('users/', UserListAPIView.as_view()),
   path('users/add/', UserCreateAPIView.as_view()),
   path('users/<int:pk>/edit/', UserUpdateAPIView.as_view()),
   path('newspapers/', NewspaperAPIView.as_view()),
   path('newspapers/<int:pk>/edit/', NewspaperUpdateAPIView.as_view()),
   path('newspapers/add/', NewspaperCreateAPIView.as_view()),
   path('offices/', PostOfficeAPIView.as_view()),
   path('offices/<int:pk>/edit/', PostOfficeUpdateAPIView.as_view()),
   path('offices/add/', PostOfficeCreateAPIView.as_view()),
   path('printeries/', PrinteryAPIView.as_view()),
   path('printeries/<int:pk>/edit/', PrinteryUpdateAPIView.as_view()),
   path('printeries/add/', PrinteryCreateAPIView.as_view()),
   path('prints/', PrintAPIView.as_view()),
   path('prints/<int:pk>/edit/', PrintUpdateAPIView.as_view()),
   path('prints/add/', PrintCreateAPIView.as_view()),
   path('parties/', NewspapersPartyAPIView.as_view()),
   path('parties/<int:pk>/edit/', NewspapersPartyUpdateAPIView.as_view()),
   path('parties/add/', NewspapersPartyCreateAPIView.as_view()),
   path('reports/', DistributionReportAPIView.as_view()),
   path('reports/<int:pk>/edit/', DistributionReportUpdateAPIView.as_view()),
   path('reports/add/', DistributionReportCreateAPIView.as_view()),
]

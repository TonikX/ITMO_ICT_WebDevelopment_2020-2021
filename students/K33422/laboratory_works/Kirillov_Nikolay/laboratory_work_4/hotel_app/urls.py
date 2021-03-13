from django.urls import path
from .views import *

app_name = "hotel_app"

urlpatterns = [
    path('rooms/list/', RoomAPIView.as_view()),
    path('rooms/info/<int:pk>/', RoomChangeAPIView.as_view()),
    path('rooms/add/', RoomAddAPIView.as_view()),
    path('staff/list/', StaffAPIView.as_view()),
    path('staff/info/<int:pk>/', StaffChangeAPIView.as_view()),
    path('staff/add/', StaffAddAPIView.as_view()),
    path('guests/list/', GuestAPIView.as_view()),
    path('guests/info/<int:pk>/', GuestChangeAPIView.as_view()),
    path('guests/add/', GuestAddAPIView.as_view()),
    path('cleanings/list/', CleaningAPIView.as_view()),
    path('cleanings/info/<int:pk>/', CleaningChangeAPIView.as_view()),
    path('cleanings/add/', CleaningAddAPIView.as_view()),
    path('users/info/<int:pk>/', UserChangeAPIView.as_view()),
    path('users/add/', UserAddAPIView.as_view()),
]

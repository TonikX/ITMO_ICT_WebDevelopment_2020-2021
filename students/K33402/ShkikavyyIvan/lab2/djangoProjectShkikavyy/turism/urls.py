from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.main),
    path('lc/', views.lc),
    path('register/', register, name='register'),
    path('reservedtour/', views.reservedtourlist),
    path('commentlist/', views.commentlist),
    path('tours/<int:pk>/createcomment', CreateComment.as_view(), name='comment'),
    path('tours/', views.tourlist),
    path('tours/<int:pk>/reservation', CreateReservation.as_view(), name='reservation'),
    path('lcreservations/', listreservations.as_view(), name='reservations'),
    path('lcreservations/lcreservations/deletereservation/<int:pk>/', views.DeleteReserveView.as_view()),
    path('lcreservations/lcreservations/updatereservation/<int:pk>/', views.UpdateReserveView.as_view())
]

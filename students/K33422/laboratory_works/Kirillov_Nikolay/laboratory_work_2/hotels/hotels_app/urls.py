from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('user/list/', UserListView.as_view(), name="user_list"),
    # path('user/add/', AddUser.as_view(success_url="http://127.0.0.1:8000/user/list/")),
    path('room/<int:pk>', views.RoomView, name="room_view"),
    path('room/list', RoomListView.as_view(), name="room_list"),
    path('hotel/list', views.HotelListView, name="hotel_list"),
    path('room/<int:pk>/reservation', views.ReservationView, name="reservation"),
    path('room/<int:pk>/delete/', views.ResDelete, name="res_delete"),
    path('', views.Index, name="index")

]

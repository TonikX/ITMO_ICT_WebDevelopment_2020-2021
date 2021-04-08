
from django.urls import path

from .views import *

urlpatterns = [
    path('', index ),
    path('accounts/register', RegisterFormView.as_view()),
    path('accounts/login/', MyLoginView.as_view()),
    path('accounts/profile/', ProfileView.as_view()),
    path('accounts/logout/', MyLogOutView.as_view(), name='logout'),
    path('hotel_list/', HotelListView.as_view(), name="home"),
    path('hotel/<int:pk>/', HotelDetailView.as_view()),
    path('room/<int:pk>/', RoomDetailView.as_view()),
    path('room/<int:pk>/reserve/', ReservateRoomView.as_view()),
    path('room/<int:pk>/add_comment/', AddCommentView.as_view()),
    path('room/<int:pk>/edit/', EditReservationView.as_view()),
    path('room/<int:pk>/delete/', DeleteReservationView.as_view()),
    path('history/', UserRoomListView.as_view()),
]

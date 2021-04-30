from django.urls import path, include

from .views import *

urlpatterns = [
    path('signup/', UserCreate.as_view(), name='register_url'),
    path('flights/', FlightList.as_view(), name='flight_list_url'),
    path('flight/<str:number>', FlightDetail.as_view(), name='flight_detail_url'),
    path('flight/<str:number>/make_a_reservation',
         ReservationCreate.as_view(), name='create_reservation_url'),
    path('my_reservations/', ReservationList.as_view(),
         name='reservation_list_url'),
    path('flight/<str:number>/edit_a_reservation/<int:pk>',
         ReservationEdit.as_view(), name="edit_reservation_url"),
    path('sign_in/', signin, name='login_url'),
    path('sign_off/', signoff, name='logout_url'),
    path('flight/<str:number>/comment',
         CommentCreate.as_view(), name='comment_url'),
    path('flight/<str:number>/passenger_list',
         PassengerList.as_view(), name="passenger_list_url"),
    path('', redirect_board),
]

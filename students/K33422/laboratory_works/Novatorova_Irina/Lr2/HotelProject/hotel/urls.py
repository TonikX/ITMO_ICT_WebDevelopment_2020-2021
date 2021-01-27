from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('registration/', registration, name='registration'),
    path('bookings/', ListBookings.as_view()),
    path('bookings/delete/<int:pk>/', DeleteBooking.as_view()),
    path('reviews', ListReviews.as_view()),
    path('hotel/list', ListHotels.as_view()),
    path('hotels/<int:pk>/', ListRooms.as_view()),
    path('rooms/<int:pk>/', RoomInfo.as_view()),
    path('rooms/<int:pk>/book', CreateBooking.as_view()),
    path('rooms/<int:pk>/add_review', CreateReview.as_view()),
    path('guests/list', ListGuests.as_view())
]
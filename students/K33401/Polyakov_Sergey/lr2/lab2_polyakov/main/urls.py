from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexPageView.as_view(), name='index_page_url'),
    path('profile/', ProfilePageView.as_view(), name='profile_page_url'),
    path('registration/', RegistrationView.as_view(), name='registration_page_url'),
    path('tours/', ToursListView.as_view(), name='tours_page_url'),
    path('tours/<int:pk>/create_comment/', CommentCreateView.as_view(), name='comment_create_page_url'),
    path('tours/<int:pk>/comments/', CommentsByTourListView.as_view(), name='comment_create_page_url'),
    path('comments/', CommentsListView.as_view(), name='comments_page_url'),
    path('reservations/', ReservationsListView.as_view(), name='reservations_page_url'),
    path('reserved/', ReservationsByUserListView.as_view(), name='reservations_user_page_url'),
    path('tours/<int:pk>/reservation', ReservationCreateView.as_view(), name='reservation_create_page_url'),
    path('reservations/<int:pk>/update/', ReservationUpdateView.as_view(), name='reservation_update_page_url'),
    path('reservations/<int:pk>/delete/', ReservationDeleteView.as_view(), name='reservation_delete_page_url'),
]

from django.urls import path
from .views import HotelsListView, hotel_view, registration, logout_view, room_view, book_view, review_view
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('', HotelsListView.as_view()),
    path('hotels/<int:hotel_id>', hotel_view),
    path('registration/', registration),
    path('login/', LoginView.as_view(template_name='login.html')),
    path('logout/', logout_view),
    path('room/<int:room_id>', room_view),
    path('book/<int:room_id>', book_view),
    path('review/<int:room_id>', review_view),
]

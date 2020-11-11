from django.urls import path 
from . import views
from django.contrib.auth.views import LoginView

# urlpatterns.append(url(r'^login/$', LoginView.as_view(template_name='login.html'), name="login"))

urlpatterns = [
    path('registration', views.guest_registration),
    path('booking', views.BookingView.as_view()),
    path('booking_delete/<pk>', views.BookingDelete.as_view()),
    path('booking_save/<pk>', views.BookingSave.as_view()),
    path('login/', LoginView.as_view(template_name='hotel/login.html')),
    path('logout', views.logout_view),
    path('booking/review/<booking_id>', views.ReviewView.as_view()),
    path('', views.table),
]
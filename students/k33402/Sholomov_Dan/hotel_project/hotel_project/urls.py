"""hotel_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from booking import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('hotels/', views.HotelsList.as_view(), name='hotels'),
    path('rooms/', views.RoomsList.as_view(), name='rooms'),
    path('hotels/<int:pk>/', views.RoomsInHotelList.as_view()),
    path('rooms/<int:pk>/', views.RoomInfo.as_view()),
    path('rooms/<int:pk>/book', views.BookRoom.as_view(), name='booking'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile_render'),
    path('profile/edit', views.profile_edit, name='profile_edit'),
    path('profile/bookings', views.BookingsList.as_view(), name='bookings'),
    path('profile/bookings/delete/<int:pk>/', views.DeleteBooking.as_view(), name='delete_booking'),
    path('reviews/', views.ReviewsList.as_view(), name='review_list'),
    path('rooms/<int:pk>/add_review', views.ReviewCreation.as_view(), name='add_review'),
    path('last_guests/', views.GuestsList.as_view(), name='last_guests'),
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html')),
    path('accounts/', include('django.contrib.auth.urls')),

]

from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('detailFuture/<int:pk>', HomeDetailViewFuture.as_view(), name='detailFuture_page'),
    path('delete_comment/<int:id>', delete_comment, name='delete_comment'),
    path('lastflight', LastFlightView.as_view(), name='flight_page'),
    path('detailPast/<int:pk>', HomeDetailViewPast.as_view(), name='detailPast_page'),
    path('login', MyprojectLoginView.as_view(), name='login_page'),
    path('logout', MyprojectLogOutView.as_view(), name='logout_page'),
    path('user', UserPage.as_view(), name='user_page'),
    path('regiser', RegisterUserView.as_view(), name='register_page'),
]


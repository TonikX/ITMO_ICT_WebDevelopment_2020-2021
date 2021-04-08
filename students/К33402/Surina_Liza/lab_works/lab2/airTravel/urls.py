from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import *

urlpatterns = [
    path('', post,  name='post_info_url'),
    path('reserve/<int:id>/', index, name='reserve'),
    path('comments/<int:id>/', comments, name="comments"),
    path('reserve/<int:id>/edit/<int:pk>/', edit),
    path('reserve/<int:id>/delete/<int:pk>', delete),
    path('login/', user_login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
]

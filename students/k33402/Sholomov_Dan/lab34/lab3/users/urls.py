from django.urls import path, include
from knox.views import LogoutView
from rest_framework import routers
from .views import (UserView, RegisterView, LoginView,
                    PasswordChangeView)

router = routers.DefaultRouter()
router.register(r'user', UserView, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/signup/', RegisterView.as_view()),
    path('auth/login/', LoginView.as_view()),
    path('auth/logout/', LogoutView.as_view()),
    path('auth/password/change/', PasswordChangeView.as_view(), name='rest_password_change'),
]
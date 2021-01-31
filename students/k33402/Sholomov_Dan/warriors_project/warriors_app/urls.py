from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

app_name = "warriors_app"

router = DefaultRouter()
router.register(r'warriors', WarriorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('profession/create/', ProfessionCreateView.as_view()),
    path('skills/', SkillAPIView.as_view()),
    path('skill/create/', SkillCreateView.as_view()),
]
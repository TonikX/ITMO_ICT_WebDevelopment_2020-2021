from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

app_name = "warriors_app"

router = DefaultRouter()
router.register(r'warriors', WarriorViewSet)

urlpatterns = [
    path('warriors/', WarriorAPIView.as_view()),
    path('warriors/create', WarriorCreateAPIView.as_view()),
    path('warriors/detail/<int:pk>', WarriorDetailsView.as_view()),
    path('warriors/delete/<int:pk>', WarriorDestroyView.as_view()),
    path('warriors/update/<int:pk>', WarriorUpdateView.as_view()),
    path('warriors/list/<int:pk>', WarriorUpdateView.as_view()),
    path('profession/create/', ProfessionCreateView.as_view()),
    path('skills/', SkillAPIView.as_view()),
    path('skill/create/', SkillCreateView.as_view()),
]
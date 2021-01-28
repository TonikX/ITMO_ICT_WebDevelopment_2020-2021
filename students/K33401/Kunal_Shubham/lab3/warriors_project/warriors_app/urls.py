from django.urls import path
from .views import *

app_name = "warriors_app"

urlpatterns = [
    path("warriors/", WarriorAPIView.as_view()),
    path("warriors/<int:warrior_id>", WarriorNestedAPIView.as_view()),
    path("warriors/update/<int:pk>", WarriorUpdateView.as_view()),
    path("warriors/delete/<int:pk>", WarriorDeleteView.as_view()),
    path("profession/create/", ProfessionCreateView.as_view()),
    path("skill", SkillAPIView.as_view()),
]
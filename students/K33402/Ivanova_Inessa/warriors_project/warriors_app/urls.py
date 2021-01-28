from django.urls import path, include
from .views import *

app_name = "warriors_app"

urlpatterns = [
    path('skills/', SkillAPIView.as_view()), # задание 1.1
    path('skills/create/', SkillCreateView.as_view()), # задание 1.1
    path('warriors/profession', WarriorAndProfessionAPIView.as_view()), # задание 2.1
    path('warriors/skill', WarriorAndSkillAPIView.as_view()), # задание 2.2
    path('warriors/<int:pk>', WarriorAPIView.as_view()), # задание 2.3
    path('warriors/<int:pk>/delete', WarriorAPIDelete.as_view()), # задание 2.4
    path('warriors/<int:pk>/update', WarriorAPIUpdate.as_view()), # задание 2.5
]


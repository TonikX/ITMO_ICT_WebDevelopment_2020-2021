from django.contrib.auth.views import LoginView
from . import views
from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('login/', LoginView.as_view(template_name='login.html')),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', registration),
    path('profile/', profile),
    path('tasks_list/', views.TasksList.as_view()),
    path('tasks_list/<int:pk>', views.TaskDescription.as_view()),

    path('completed_tasks/', views.CompletedTask.as_view()),
    path('completed_tasks/<int:pk>/add/', views.AddSubmission.as_view(success_url="/completed_tasks/")),
    path('completed_tasks/<int:pk>/update/', views.SubmissionUpdate.as_view(success_url="/completed_tasks/")),
    path('completed_tasks/<int:pk>/delete/', views.SubmissionDelete.as_view(success_url="/completed_tasks/")),

    path('grades/', views.GradesTable.as_view()),
]
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.register_page, name="register"),

    path('tasks_list/', views.TasksList.as_view()),
    path('tasks_list/<int:pk>', views.TaskDescription.as_view()),

    path('completed_tasks/', views.CompletedTask.as_view()),

    path('completed_tasks/<int:pk>/add/', views.AddSubmission.as_view(success_url="/completed_tasks/")),
    path('completed_tasks/<int:pk>/update/', views.SubmissionUpdate.as_view()),
    path('completed_tasks/<int:pk>/delete/', views.SubmissionDelete.as_view()),
    path('grades/', views.GradesTable.as_view()),
]
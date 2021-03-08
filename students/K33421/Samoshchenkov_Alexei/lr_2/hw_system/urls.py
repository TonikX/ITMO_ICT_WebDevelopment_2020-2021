from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('homeworks/', views.HomeworksList.as_view()),
    path('homeworks/<int:pk>', views.HomeworkDetail.as_view()),
    path('answers/', views.AnswersList.as_view()),
    path('answers/<int:pk>/add/', views.AddAnswer.as_view(success_url="/answers/")),
    path('answers/<int:pk>/update/', views.AnswerUpdate.as_view(success_url="/answers/")),
    path('answers/<int:pk>/delete/', views.AnswerDelete.as_view(success_url="/answers/")),
    path('grades/', views.GradesTable.as_view()),
]
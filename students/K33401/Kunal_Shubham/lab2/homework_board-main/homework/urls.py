from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login', views.LoginView.as_view(), name='login_view'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('register', views.RegistrationView.as_view(), name='register'),
    path('submissions', views.SubmissionView.as_view(), name='submission_list'),
    path('leaderboard', views.LeaderboardView.as_view(), name='leaderboard_list'),
    path('assignment/<int:pk>', views.AssignmentDetailView.as_view(),
         name='assignment-detail'),
    path('assignment/<int:assignment_id>/submit',
         views.AssignmentSubmission, name='assignment_submit'),
]

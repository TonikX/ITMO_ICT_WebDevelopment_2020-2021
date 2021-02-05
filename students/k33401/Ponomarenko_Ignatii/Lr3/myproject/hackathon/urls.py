from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('registration', views.registration),
    path('login/', LoginView.as_view(template_name='hackathon/login.html')),
    path('', views.TasksView.as_view()),
    path('tasks/<pk>/solution-create', views.SolutionCreateView.as_view()),
    path('tasks/<pk>/solution-update', views.SolutionUpdateView.as_view()),
    path('tasks/create', views.TaskCreateView.as_view()),
    path('logout', views.logout_view),
    path('profile', views.profile),
    path('team', views.team),
]


urlpatterns += staticfiles_urlpatterns()
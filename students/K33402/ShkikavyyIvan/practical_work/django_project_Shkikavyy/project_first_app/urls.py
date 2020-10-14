from django.urls import path
from . import views

urlpatterns = [ path('owner/', views.detail),
    path('autos/', views.AutoList.as_view()),
    path('auto/<int:pk>/', views.AutoDetailView.as_view()),
    path('create_owner/', views.create_owner_view),
    path('create_auto/', views.AutoCreate.as_view()),
    path('auto/<int:pk>/update/', views.AutoUpdateView.as_view()),
    path('auto/<int:pk>/delete/', views.AutoDeleteView.as_view()),]



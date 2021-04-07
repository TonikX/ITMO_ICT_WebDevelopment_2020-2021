from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('owner/<int:owner_id>', views.detail),
    path('carowners/', views.get_carowners),
    path('carowners/create_carowner/', views.create_carowner),
    path('car/list/', CarList.as_view()),
    path('car/<int:pk>/', CarRetrieveView.as_view()),
    path('car/<int:pk>/update/', CarUpdateView.as_view()),
    path('car/create/', CarCreateView.as_view()),
    path('car/<int:pk>/delete/', CarDeleteView.as_view())
]

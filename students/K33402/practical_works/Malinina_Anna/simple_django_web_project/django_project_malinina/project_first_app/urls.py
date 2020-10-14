from django.urls import path
from .views import *

urlpatterns = [
    path('owner/<int:owner_id>/', get_owner),
    path('owners/', get_owners),
    path('cars/', CarsListView.as_view()),
    path('car/<int:pk>/', CarDetailView.as_view()),
    path('car/<int:pk>/update/', CarUpdateView.as_view()),
    path('owner/create/', create_view),
    path('car/create/', CarCreate.as_view()),
    path('car/<int:pk>/delete/', CarDeleteView.as_view()),
]

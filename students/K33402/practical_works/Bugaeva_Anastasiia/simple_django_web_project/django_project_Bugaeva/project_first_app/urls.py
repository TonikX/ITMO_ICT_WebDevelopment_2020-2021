from django.urls import path
from .views import *

urlpatterns = [
    path('owner/<int:owner_id>/', get_owner),
    path('all_owners/', get_owners),
    path('cars_list/', CarsList.as_view()),
    path('car/<int:pk>/', CarDetails.as_view()),
    path('owner/creating/', create_view),
    path('car/creating/', CarCreate.as_view()),
    path('car/<int:pk>/updating/', CarUpdate.as_view()),
    path('car/<int:pk>/deleting/', CarDelete.as_view()),
]

from django.urls import path
from .views import *

urlpatterns = [
    path('owner/<int:owner_id>/', get_owner),
]
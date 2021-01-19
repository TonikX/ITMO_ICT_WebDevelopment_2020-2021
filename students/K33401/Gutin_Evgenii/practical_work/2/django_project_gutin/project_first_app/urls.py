from . import views
from .views import VehicleView, VehicleDelete, VehicleUpdate, VehicleCreate
from django.urls import path

urlpatterns = [
    path('owners/<int:owner_id>', views.get_owner_by_id),
    path('owners/all', views.get_owners),
    path('vehicle/', VehicleView.as_view()),
    path('vehicle/<int:pk>/delete/', VehicleDelete.as_view()),
    path('vehicle/<int:pk>/edit/', VehicleUpdate.as_view()),
    path('vehicle/create/', VehicleCreate.as_view()),
    path('owners/create', views.create_owner)
]

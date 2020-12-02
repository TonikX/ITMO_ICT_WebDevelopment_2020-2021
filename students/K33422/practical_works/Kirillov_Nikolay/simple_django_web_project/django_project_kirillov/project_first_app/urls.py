from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('driver/<int:driver_id>', views.DriverDetail),
    path('driver/list/', DriverListView),
    path('add_driver/', DriverCreate),
    path('car/<int:car_id>', views.CarDetail),
    path('car/list/', CarListView.as_view()),
    path('car/<int:pk>/update/', CarUpdateView.as_view(success_url="http://127.0.0.1:8000/car/list/")),
    path('add_car/', CarCreate.as_view(success_url="http://127.0.0.1:8000/car/list/")),
    path('car/<int:pk>/delete/', CarDeleteView.as_view(success_url="http://127.0.0.1:8000/car/list/")),

]

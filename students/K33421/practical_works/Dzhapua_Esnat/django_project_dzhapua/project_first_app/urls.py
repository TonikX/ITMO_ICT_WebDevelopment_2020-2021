from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('carowner_id/<int:carowner_id>', views.CarownerView),
    path('car_id/<int:car_id>', views.CarView),
    path('carowner_list/', CarownerListView),
    path('car_list/', CarListView.as_view()),
    path('car_add/', CarAddView.as_view(success_url="http://127.0.0.1:8000/car_list/")),
    path('car_edit/<int:pk>', CarEditView.as_view(success_url="http://127.0.0.1:8000/car_list/")),
    path('car_del/<int:pk>', CarDelView.as_view(success_url="http://127.0.0.1:8000/car_list/")),
    path('carowner_add/', CarownerAdd),

]
from django.urls import path, include
from django_first_app.views import *
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('owner/<int:id>/', detail, name='name_page_url'),
    path('drivers/', show_drivers),
    path('drivers/create', create_driver),
    path('cars/create', CarCreate.as_view()),
    path('cars/', CarList.as_view()),
    path('cars/<int:pk>', CarDetail.as_view()),
    path('cars/<int:pk>/update', CarUpdate.as_view()),
    path('cars/<int:pk>/delete', CarDelete.as_view()),
]

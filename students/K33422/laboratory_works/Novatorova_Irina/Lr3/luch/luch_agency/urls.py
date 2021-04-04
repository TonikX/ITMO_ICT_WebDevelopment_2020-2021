from django.urls import path
from .views import *

app_name = "luch_agency"

urlpatterns = [
    path('user/list', UserListAPIView.as_view()),
    path('user/<int:pk>/', UserEditAPIView.as_view()),

    path('application/list', ApplicationNestedAPIView.as_view()),
    path('application/<int:pk>/', ApplicationEditAPIView.as_view()),
    path('application/create/', ApplicationCreateAPIView.as_view()),

    path('application_list/list', ApplicationListNestedAPIView.as_view()),

    path('client/list', ClientListAPIView.as_view()),
    path('client/<int:pk>/', ClientEditAPIView.as_view()),
    path('client/create/', ClientCreateAPIView.as_view()),

    path('manufactory/list', ManufactoryNestedAPIView.as_view()),
    path('manufactory/<int:pk>/', ManufactoryEditAPIView.as_view()),

    path('material/list', MaterialListAPIView.as_view()),
    path('material/<int:pk>/', MaterialEditAPIView.as_view()),
    path('material/create/', MaterialCreateAPIView.as_view()),

    path('payment_order/list', PaymentOrderNestedAPIView.as_view()),

    path('service/list', ServiceListAPIView.as_view()),
    path('service/<int:pk>/', ServiceEditAPIView.as_view()),
    path('service/create/', ServiceCreateAPIView.as_view()),

    path('worker/list', WorkerListAPIView.as_view()),
    path('worker/<int:pk>/', WorkerEditAPIView.as_view()),
    path('worker/create/', WorkerCreateAPIView.as_view()),
    ]
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('car_owner/<int:id>/', views.detail),
    path('example_list/', views.list_view),
    path('сvb_example/', ExampleList.as_view()),
    path('publisher/<int:pk>/', PublisherRetrieveView.as_view()),
    path('example_create/', create_view),
    path('car_owner/<int:pk>/update', CarOwnerUpdateView.as_view()),
    path('car', CarCreate.as_view(success_url="/сvb_example/"))

]


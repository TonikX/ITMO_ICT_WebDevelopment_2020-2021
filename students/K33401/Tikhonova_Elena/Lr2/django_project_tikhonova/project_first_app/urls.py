from django.urls import path
from .views import owner, car, home, detail

urlpatterns = [
    path('owner/', owner),
    path('owner/<owner_id>', detail),
    path('car/', car),
    path('', home),
]

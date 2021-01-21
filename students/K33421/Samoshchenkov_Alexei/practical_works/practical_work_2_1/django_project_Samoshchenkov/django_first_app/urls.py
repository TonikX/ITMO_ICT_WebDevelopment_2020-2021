from django.urls import path
from django_first_app.views import *

urlpatterns = [
    path('owner/<int:id>/', detail, name='name_page_url')
]
from django.urls import path, include
from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('homeworks/', views.homeworks, name='homeworks'),
#    path('owner/<int:number>', views.owner, name='owner'),
]
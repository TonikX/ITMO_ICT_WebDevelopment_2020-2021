from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import LostViewSet

router = DefaultRouter()
router.register(r"", LostViewSet, basename="lost")

urlpatterns = [
    path("", include(router.urls)),
]
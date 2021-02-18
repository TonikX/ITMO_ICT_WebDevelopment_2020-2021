from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import OrdersViewSet, OrderedItemsViewSet

router = DefaultRouter()
router.register(r"orders", OrdersViewSet, basename="orders")
router.register(r"ordereditems", OrderedItemsViewSet, basename="ordereditems")


urlpatterns = [
    path("", include(router.urls)),
]
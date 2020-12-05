from django.urls import path, include
from rest_framework.routers import DefaultRouter

from polls_app.views import UserViewSet, PollViewSet

router = DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'poll', PollViewSet)

urlpatterns = [
    path('', include(router.urls))
]

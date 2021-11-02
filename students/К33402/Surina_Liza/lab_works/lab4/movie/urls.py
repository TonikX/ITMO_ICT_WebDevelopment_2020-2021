from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import ClientViewSet, ReviewCreateView, MovieDetailView

router = DefaultRouter()
router.register("movies", ClientViewSet, basename="movies")

urlpatterns = [
    path('', include(router.urls)),
    path("review/", ReviewCreateView.as_view()),
    path("movies/<int:pk>/", MovieDetailView.as_view()),
]
